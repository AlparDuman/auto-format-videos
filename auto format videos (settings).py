#PY  <- Needed to identify #
#--automatically built--

adm = Avidemux()
adm.setHDRConfig(1, 1, 1, 1, 0)
adm.videoCodec("x264", "useAdvancedConfiguration=False", "general.params=AQ=20", "general.threads=0", "general.preset=placebo", "general.tuning=none", "general.profile=high", "general.fast_decode=False", "general.zero_latency=False"
, "general.fast_first_pass=true", "general.blueray_compatibility=False", "general.fake_interlaced=False", "level=51", "vui.sar_height=1", "vui.sar_width=1", "vui.overscan=0", "vui.vidformat=5", "vui.fullrange=False"
, "vui.colorprim=2", "vui.transfer=2", "vui.colmatrix=2", "vui.chroma_loc=0", "MaxRefFrames=3", "MinIdr=25", "MaxIdr=250", "i_scenecut_threshold=40", "intra_refresh=False", "MaxBFrame=3", "i_bframe_adaptive=1"
, "i_bframe_bias=0", "i_bframe_pyramid=2", "b_deblocking_filter=True", "i_deblocking_filter_alphac0=0", "i_deblocking_filter_beta=0", "cabac=True", "interlaced=False", "constrained_intra=False", "tff=True"
, "fake_interlaced=False", "analyze.b_8x8=True", "analyze.b_i4x4=True", "analyze.b_i8x8=True", "analyze.b_p8x8=True", "analyze.b_p16x16=False", "analyze.b_b16x16=False", "analyze.weighted_pred=2", "analyze.weighted_bipred=True"
, "analyze.direct_mv_pred=1", "analyze.chroma_offset=0", "analyze.me_method=1", "analyze.me_range=16", "analyze.mv_range=-1", "analyze.mv_range_thread=-1", "analyze.subpel_refine=7", "analyze.chroma_me=True"
, "analyze.mixed_references=True", "analyze.trellis=1", "analyze.psy_rd=1.000000", "analyze.psy_trellis=0.000000", "analyze.fast_pskip=True", "analyze.dct_decimate=True", "analyze.noise_reduction=0", "analyze.psy=True"
, "analyze.intra_luma=11", "analyze.inter_luma=21", "ratecontrol.rc_method=0", "ratecontrol.qp_constant=0", "ratecontrol.qp_min=10", "ratecontrol.qp_max=51", "ratecontrol.qp_step=4", "ratecontrol.bitrate=0"
, "ratecontrol.rate_tolerance=1.000000", "ratecontrol.vbv_max_bitrate=0", "ratecontrol.vbv_buffer_size=0", "ratecontrol.vbv_buffer_init=1", "ratecontrol.ip_factor=1.400000", "ratecontrol.pb_factor=1.300000"
, "ratecontrol.aq_mode=1", "ratecontrol.aq_strength=1.000000", "ratecontrol.mb_tree=True", "ratecontrol.lookahead=40")
adm.audioClearTracks()

if 1 <= adm.audioTotalTracksCount():
    adm.setSourceTrackLanguage(0,"System sound")
    adm.audioAddTrack(0)
    adm.audioCodec(0, "LavAAC", "bitrate=384")
    adm.audioSetResample(0, 48000)
    adm.audioSetDrc2(0, 0, 1, 0.001, 0.2, 1, 2, -12)
    adm.audioSetEq(0, 0, 0, 0, 0, 880, 5000)
    adm.audioSetChannelGains(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    adm.audioSetChannelDelays(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    adm.audioSetChannelRemap(0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8)
    adm.audioSetShift(0, 0, 0)
    adm.audioSetNormalize2(0, 1, 10, -30)

if 2 <= adm.audioTotalTracksCount():
    adm.setSourceTrackLanguage(1,"Microphone")
    adm.audioAddTrack(1)
    adm.audioCodec(1, "LavAAC", "bitrate=384")
    adm.audioSetResample(1, 48000)
    adm.audioSetDrc2(1, 0, 1, 0.001, 0.2, 1, 2, -12)
    adm.audioSetEq(1, 0, 0, 0, 0, 880, 5000)
    adm.audioSetChannelGains(1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    adm.audioSetChannelDelays(1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    adm.audioSetChannelRemap(1, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8)
    adm.audioSetShift(1, 0, 0)
    adm.audioSetNormalize2(1, 1, 10, -30)

if 3 <= adm.audioTotalTracksCount():
    adm.setSourceTrackLanguage(2,"extra 3")
    adm.audioAddTrack(2)
    adm.audioCodec(2, "LavAAC", "bitrate=384")
    adm.audioSetResample(2, 48000)
    adm.audioSetDrc2(2, 0, 1, 0.001, 0.2, 1, 2, -12)
    adm.audioSetEq(2, 0, 0, 0, 0, 880, 5000)
    adm.audioSetChannelGains(2, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    adm.audioSetChannelDelays(2, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    adm.audioSetChannelRemap(2, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8)
    adm.audioSetShift(2, 0, 0)
    adm.audioSetNormalize2(2, 1, 10, -30)

if 4 <= adm.audioTotalTracksCount():
    adm.setSourceTrackLanguage(3,"extra 4")
    adm.audioAddTrack(3)
    adm.audioCodec(3, "LavAAC", "bitrate=384")
    adm.audioSetResample(3, 48000)
    adm.audioSetDrc2(3, 0, 1, 0.001, 0.2, 1, 2, -12)
    adm.audioSetEq(3, 0, 0, 0, 0, 880, 5000)
    adm.audioSetChannelGains(3, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    adm.audioSetChannelDelays(3, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    adm.audioSetChannelRemap(3, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8)
    adm.audioSetShift(3, 0, 0)
    adm.audioSetNormalize2(3, 1, 10, -30)

if 5 <= adm.audioTotalTracksCount():
    adm.setSourceTrackLanguage(4,"extra 5")
    adm.audioAddTrack(4)
    adm.audioCodec(4, "LavAAC", "bitrate=384")
    adm.audioSetResample(4, 48000)
    adm.audioSetDrc2(4, 0, 1, 0.001, 0.2, 1, 2, -12)
    adm.audioSetEq(4, 0, 0, 0, 0, 880, 5000)
    adm.audioSetChannelGains(4, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    adm.audioSetChannelDelays(4, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    adm.audioSetChannelRemap(4, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8)
    adm.audioSetShift(4, 0, 0)
    adm.audioSetNormalize2(4, 1, 10, -30)

if 6 <= adm.audioTotalTracksCount():
    adm.setSourceTrackLanguage(5,"extra 6")
    adm.audioAddTrack(5)
    adm.audioCodec(5, "LavAAC", "bitrate=384")
    adm.audioSetResample(5, 48000)
    adm.audioSetDrc2(5, 0, 1, 0.001, 0.2, 1, 2, -12)
    adm.audioSetEq(5, 0, 0, 0, 0, 880, 5000)
    adm.audioSetChannelGains(5, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    adm.audioSetChannelDelays(5, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    adm.audioSetChannelRemap(5, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8)
    adm.audioSetShift(5, 0, 0)
    adm.audioSetNormalize2(5, 1, 10, -30)

if 7 <= adm.audioTotalTracksCount():
    adm.setSourceTrackLanguage(6,"extra 7")
    adm.audioAddTrack(6)
    adm.audioCodec(6, "LavAAC", "bitrate=384")
    adm.audioSetResample(6, 48000)
    adm.audioSetDrc2(6, 0, 1, 0.001, 0.2, 1, 2, -12)
    adm.audioSetEq(6, 0, 0, 0, 0, 880, 5000)
    adm.audioSetChannelGains(6, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    adm.audioSetChannelDelays(6, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    adm.audioSetChannelRemap(6, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8)
    adm.audioSetShift(6, 0, 0)
    adm.audioSetNormalize2(6, 1, 10, -30)

if 8 <= adm.audioTotalTracksCount():
    adm.setSourceTrackLanguage(7,"extra 8")
    adm.audioAddTrack(7)
    adm.audioCodec(7, "LavAAC", "bitrate=384")
    adm.audioSetResample(7, 48000)
    adm.audioSetDrc2(7, 0, 1, 0.001, 0.2, 1, 2, -12)
    adm.audioSetEq(7, 0, 0, 0, 0, 880, 5000)
    adm.audioSetChannelGains(7, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    adm.audioSetChannelDelays(7, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    adm.audioSetChannelRemap(7, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8)
    adm.audioSetShift(7, 0, 0)
    adm.audioSetNormalize2(7, 1, 10, -30)

adm.setContainer(
    "MP4",
    "muxerType=0",
    "optimize=1",
    "forceAspectRatio=False",
    "aspectRatio=1",
    "displayWidth=1280",
    "rotation=0",
    "clockfreq=0"
    )
