import unreal
from unreal import EditorLevelLibrary, LevelEditorSubsystem, LevelSequenceEditorBlueprintLibrary

level_editor = LevelEditorSubsystem()
success = level_editor.load_level('/Game/default_world')

# Note: no '.uasset' extension!
mh_asset_path = "/Game/MetaHumans/Chandra/BP_Chandra"
mh_asset = unreal.load_asset(mh_asset_path)

# Note: rotate 90 deg around Z to face default camera of viewport
spawned_actor = EditorLevelLibrary.spawn_actor_from_class(
  mh_asset.generated_class(),
  location=unreal.Vector(0, 0, 0),
  rotation=unreal.Rotator(0, 0, 90)
)

level_sequence = unreal.load_asset("/Game/default_sequence")

factory = unreal.LevelSequenceFactoryNew()
asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
level_sequence = asset_tools.create_asset(
    'test_sequence',
    '/Game',
    unreal.LevelSequence,
    factory
)

LevelSequenceEditorBlueprintLibrary.open_level_sequence(level_sequence)

frame_rate = unreal.FrameRate(numerator=60, denominator=1)
level_sequence.set_display_rate(frame_rate)
level_sequence.set_playback_start(0)
level_sequence.set_playback_end(60 * 5)  # 5 seconds

level_sequence_editor = unreal.get_editor_subsystem(unreal.LevelSequenceEditorSubsystem)
movie_scene, camera_actor = level_sequence_editor.create_camera(spawnable=False)
LevelSequenceEditorBlueprintLibrary.set_lock_camera_cut_to_viewport(True)
camera_comp = camera_actor.get_cine_camera_component()
camera_comp.focus_settings.focus_method = camera_comp.focus_settings.focus_method.DISABLE
#camera_comp.focus_settings.tracking_focus_settings.actor_to_track = spawned_actor

level_sequence_editor.add_actors([spawned_actor])
rig = unreal.load_asset('/Game/MetaHumans/Common/Common/MetaHuman_ControlRig')
rig_class = rig.get_control_rig_class()

body_rig, face_rig = unreal.ControlRigSequencerLibrary.get_control_rigs(level_sequence)
face_rig_ = face_rig.control_rig
face_rig_.select_control("CTRL_R_mouth_corner")
#h = face_rig_.get_hierarchy()
#print(h.get_controls())
start = unreal.FrameNumber(0)
unreal.ControlRigSequencerLibrary.set_local_control_rig_vector2d(level_sequence, face_rig_, "CTRL_R_mouth_corner", start, unreal.Vector2D(0., 0.))
unreal.ControlRigSequencerLibrary.set_local_control_rig_vector2d(level_sequence, face_rig_, "CTRL_L_mouth_corner", start, unreal.Vector2D(0., 0.))

end = unreal.FrameNumber(299)
out = unreal.ControlRigSequencerLibrary.set_local_control_rig_vector2d(level_sequence, face_rig_, "CTRL_R_mouth_corner", end, unreal.Vector2D(0., -1.))
unreal.ControlRigSequencerLibrary.set_local_control_rig_vector2d(level_sequence, face_rig_, "CTRL_L_mouth_corner", end, unreal.Vector2D(0., -1.))

# Create an instance of UAutomatedLevelSequenceCapture
capture_settings = unreal.AutomatedLevelSequenceCapture()
capture_settings.level_sequence_asset = unreal.SoftObjectPath('/Game/test_sequence')
unreal.SequencerTools.render_movie(capture_settings, unreal.OnRenderMovieStopped())
