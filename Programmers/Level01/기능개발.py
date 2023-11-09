# 2023년 11월 09일 목요일
# 스택/큐

# 문제 분석
# 작업마다 속도가 다르다.
# 작업이 다 끝나도 먼저 들어온 작업이 마쳐지지 않으면 배포될 수 없다. -> 선입선출(큐)
# 배포시 몇 개의 작업이 배포되는지 return한다.

def solution(progresses, speeds):
    
    answer = []
    days = 0
    cnt = 0
    
    while len(progresses) > 0:
        
        # 만약에 작업이 완료되어 배포가 가능하다면?
        if progresses[0] + (speeds[0] * days) >= 100:
            # 작업 배열에서 삭제하고
            progresses.pop(0)
            speeds.pop(0)
            # 배포 가능한 개수를 +1한다.
            cnt += 1
        # 만약에 작업이 완료되지 않았다면?
        else:
            # 이전에 작업한 내용이 있다면 걔들은 먼저 배포하고
            if(cnt > 0):
                answer.append(cnt)
                cnt = 0
            # 이전에 작업한 내용이 없다면 내가 첫빠로 배포 될 예정이니
            # 시간을 계속 늘려가면서 배포 되는지 체크
            days += 1
            
    # 반복문이 끝나고 마지막 배포 될 친구들이 아직 남아있을 수 있어서
    if(cnt > 0):
        answer.append(cnt)

    return answer