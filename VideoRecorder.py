import cv2

def apply_filter(frame, filter_type):
    """필터를 적용하는 함수."""
    if filter_type == '1':  # 밝기 증가
        return cv2.convertScaleAbs(frame, alpha=1.2, beta=30), "Brightness Increased"
    elif filter_type == '2':  # 대비 증가
        return cv2.convertScaleAbs(frame, alpha=1.5, beta=0), "Contrast Increased"
    elif filter_type == '3':  # 가로로 반전
        return cv2.flip(frame, 1), "Flipped Horizontally"
    else:  # 필터 없음
        return frame, "No Filter"

def start_rtsp_recording(rtsp_url):
    # RTSP 스트림 열기
    cap = cv2.VideoCapture(rtsp_url)

    if not cap.isOpened():
        print(f"Failed to open RTSP stream: {rtsp_url}")
        return

    # VideoWriter 초기 설정
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = None
    recording = False  # 녹화 상태 변수
    filter_type = '0'  # 기본 필터 없음
    filter_name = "No Filter"  # 필터 이름 초기화

    print("Press '1' for brightness, '2' for contrast, '3' for flip, '0' for no filter.")
    print("Press 'SPACE' to start/stop recording, 'ESC' to exit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        # 필터 적용
        filtered_frame, filter_name = apply_filter(frame, filter_type)

        # 키 입력 처리
        key = cv2.waitKey(1) & 0xFF

        # ESC 키: 종료
        if key == 27:  # ESC key
            break

        # Space 키: 녹화 시작/정지 전환
        elif key == 32:  # SPACE key
            recording = not recording
            if recording:
                print("Recording started...")
                out = cv2.VideoWriter('rtsp_filtered_record.avi', fourcc, 20.0,
                                      (filtered_frame.shape[1], filtered_frame.shape[0]))
            else:
                print("Recording stopped.")
                if out:
                    out.release()

        # 녹화 중일 때 빨간 원과 필터 이름 표시
        if recording:
            # 빨간 원을 그려서 녹화 중임을 알림
            cv2.circle(filtered_frame, (610, 30), 20, (0, 0, 255), -1)
            # 필터 이름을 프레임에 표시
            cv2.putText(filtered_frame, f"Filter: {filter_name}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
            # 필터가 적용된 프레임을 파일에 저장
            out.write(filtered_frame)

        # 필터 선택 (녹화 중에도 가능)
        if key in [ord('0'), ord('1'), ord('2'), ord('3')]:
            filter_type = chr(key)
            print(f"Filter set to: {filter_type}")
            
        # 필터 이름을 프레임에 표시
        #cv2.putText(filtered_frame, f"Filter: {filter_name}", (10, 30),
        #            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

        # 필터가 적용된 프레임을 화면에 표시
        cv2.imshow('RTSP Stream with Filters', filtered_frame)

    # 자원 해제 및 창 닫기
    cap.release()
    if out:
        out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # 사용자로부터 RTSP 주소 입력 받기
    rtsp_url = input("Enter RTSP URL: ").strip()
    if rtsp_url:
        start_rtsp_recording(rtsp_url)
    else:
        print("No RTSP URL provided. Exiting.")
