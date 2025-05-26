from flask import Flask, render_template, request, redirect

app = Flask(__name__, static_folder='static', static_url_path='/static')

# 스트레칭 팁 목록 (전광판에 표시될 내용)
STRETCHING_TIPS = [
    "스트레칭은 꾸준히 하는 것이 중요해요!",
    "무리한 스트레칭은 부상을 유발할 수 있어요. 통증이 느껴지면 즉시 중단하세요.",
    "스트레칭 전후에는 가벼운 워밍업과 쿨다운을 해주세요.",
    "호흡을 잊지 마세요! 스트레칭 중에는 부드럽게 숨을 쉬는 것이 중요해요.",
    "자세 유지 시 15~30초 정도 버티는 것이 좋아요.",
    "아침 스트레칭은 몸을 깨우고 유연성을 높여줘요.",
    "자기 전 스트레칭은 숙면을 돕고 피로를 풀어줘요.",
    "스트레칭으로 혈액순환을 개선하고 근육 긴장을 완화하세요.",
    "매일 10분씩 투자하면 몸이 훨씬 가벼워질 거예요!",
    "스트레칭은 자세 교정에도 도움을 줍니다."
]


STRETCHES = {
    '누운 자세': [
        ("침대 10분 스트레칭", "4lDgU7tc3dI", "lying_stretch_bed1.jpg"),
        ("침대 10분 스트레칭(2)", "sJ8aGq898DA", "lying_stretch_bed2.jpg"),
        ("15분 스트레칭", "s0YLzNmMQOg", "lying_stretch_15min.jpg"),
    ],
    '앉은 자세': [
        ("두통 완화 스트레칭", "FjFFasD3kr0", "sitting_stretch_headache.jpg"),
        ("10분 스트레칭", "FvGTFMaPcxk", "sitting_stretch_10min.jpg"),
        ("의자 스트레칭", "n0sCHcQK4_0", "sitting_stretch_chair.jpg"),
        ("허리 통증 완화 스트레칭", "bEDH_uTcdf4", "sitting_stretch_back.jpg"),
    ],
    '서 있는 자세': [
        ("8분 전신 스트레칭", "33VsVMf8Hgk", "standing_stretch_8min.jpg"),
        ("10분 전신 스트레칭", "npNod6rVZrs", "standing_stretch_10min.jpg"),
        ("6분 전신 스트레칭", "4Gs_23332M4", "standing_stretch_6min.jpg"),
    ]
}

# 비디오 ID에 따른 상세 정보 딕셔너리 (stretch_detail 라우트에서 사용)
# 이 정보를 통해 video_title과 video_pose를 템플릿으로 전달합니다.
VIDEO_DETAILS = {
    "4lDgU7tc3dI": {"title": "침대 10분 스트레칭", "pose": "누운 자세"},
    "sJ8aGq898DA": {"title": "침대 10분 스트레칭(2)", "pose": "누운 자세"},
    "s0YLzNmMQOg": {"title": "15분 스트레칭", "pose": "누운 자세"},
    "FjFFasD3kr0": {"title": "두통 완화 스트레칭", "pose": "앉은 자세"},
    "FvGTFMaPcxk": {"title": "10분 스트레칭", "pose": "앉은 자세"},
    "n0sCHcQK4_0": {"title": "의자 스트레칭", "pose": "앉은 자세"},
    "bEDH_uTcdf4": {"title": "허리 통증 완화 스트레칭", "pose": "앉은 자세"},
    "33VsVMf8Hgk": {"title": "8분 전신 스트레칭", "pose": "서 있는 자세"},
    "npNod6rVZrs": {"title": "10분 전신 스트레칭", "pose": "서 있는 자세"},
    "4Gs_23332M4": {"title": "6분 전신 스트레칭", "pose": "서 있는 자세"},
}


@app.route('/')
def index():
    """메인 화면: 자세 선택 버튼을 보여줍니다."""
    # STRETCHING_TIPS 리스트를 'tips'라는 변수명으로 템플릿에 전달
    return render_template('index.html', tips=STRETCHING_TIPS)

@app.route('/stretches/<pose>')
def show_stretches(pose):
    """
    선택한 자세에 맞는 스트레칭 목록을 보여줍니다.
    존재하지 않는 자세일 경우 메인으로 리디렉션합니다.
    """
    if pose in STRETCHES:
        stretching_list = STRETCHES[pose]
        # 'pose', 'stretches', 그리고 'tips' 변수를 템플릿으로 넘겨줍니다.
        return render_template('stretch_list.html', pose=pose, stretches=stretching_list, tips=STRETCHING_TIPS)
    else:
        # 유효하지 않은 자세는 메인으로 리디렉션
        return redirect('/')

# 새로 추가되는 라우트: 스트레칭 상세 페이지
@app.route('/stretch_detail/<video_id>')
def stretch_detail(video_id):
    """
    특정 유튜브 영상 ID를 받아와 해당 영상을 임베드하여 보여줍니다.
    """
    # VIDEO_DETAILS 딕셔너리에서 해당 video_id의 정보를 가져옵니다.
    # .get()을 사용하여 video_id가 없으면 기본값을 반환하도록 합니다.
    detail = VIDEO_DETAILS.get(video_id, {"title": "알 수 없는 스트레칭", "pose": "알 수 없음"})
    
    # video_id, video_title, video_pose, 그리고 'tips' 변수를 템플릿으로 넘겨줍니다.
    return render_template('stretch_detail.html', 
                           video_id=video_id, 
                           video_title=detail['title'], 
                           video_pose=detail['pose'],
                           tips=STRETCHING_TIPS)


if __name__ == '__main__':
    app.run(debug=True)