### 투 포인터(Two Pointer)

- 연속 부분 수열  등장
    - 누적합 혹은 투포인터일 확률이 높음
- 완전탐색이 가능하다면 완전탐색으로 우선 생각하기(가장 중요)
- 투포인터를 사용하는 경우
    - 조건을 만족하는 두 수를 찾을 때
    - 조건을 만족하는 연속된 구간 찾을 때
    - ~~정렬된 두 배열을 합칠 때 (해당 주제는 잘 출제되지 않음)~~
- 투 포인터의 주요 아이디어
    - 후보에서 지운다
    - (상황에따라) 배열을 정렬
    - 특정 조건을 만족하는 두 수
        - s = 0, e = n-1이라 하고
        - s 와 e 가 만날 때 까지 반복할 건데
        - s, e 중에 후보에서 빠져야하는게 있으면 → 그것을 지운다
- 기본적인 틀

    ```python
    s = 0
    e = n-1
    while s < e:
    	if ls[s] + ls[e] == x:
    			cnt += 1
    			s += 1
    			e -= 1
    	elif ls[s] + ls[e] < x:
    			s += 1
    	else :
    		e -= 1
    ```


### 조건을 만족하는 두 수

- 백준 3273번 두 수의 합

    ```python
    """
    # 합이 13인 경우
    1 2 3 5 7 9 10 11 12 14
    
    # 정답이 될 가능성이 있는 후보
    1 2 3 5 7 9 10 11 12 14
    S                     E -> 초기 상태 [S,E] : 정답 후보의 범위 
    """
    """
    만약 S + E = 14 인 상황이라면 
    """
    
    # 잘못된 설명
    """
    수를 줄여야하니까 E를 왼쪽으로 이동시켜준다
    """
    
    # 옳은 설명(상황을 더 엄밀하게 파악해야함)
    """
    1. 현재 배열은 정렬 되어 있음
    2. s,e 두 개의 포인터를 사용 → 양 끝에 위치  
    3. [s,e] ⇒ 정답 후보의 범위 
    4. s 입장에서는 정답 후보 중 가장 큰 값과 더했다 
    5. e 입장에서는 정답 후보 중 가장 작은 값과 더했다
    6. s가 가장 큰 값과 더했을 때 정답 보다 크다 그렇다면 e 입장에서는 s가 아닌 다른 값들은 누구랑 더해도 답이 될 수 가 없다!! 따라서 e가 앞으로 옮겨져야 함
    """
    
    """
    1 2 3 5 7 9 10 11 12 
    S                 E     -> 정답인 경우 cnt += 1
    
    1이 12를 찾았을 때 그 다음은 정답이 될 수 없다
    따라서 S += 1, E -= 1
    다음 과정을 반복해준다 
            
    """
    ```

- 백준 20366번 같이 눈사람 만들래
    - 완전 탐색

        ```python
        
        n = int(input())
        ls = list(map(int, input().split()))
        
        for i in range(n):
        	for j in range(n):
        		for k in range(n): 
        			for l in range(n):
        				if i == j or i == k or j ==k or j == l or k ==l:
        					continue
        				ans = min(ans, abs(ls[i] - ls[j] - (ls[k] - ls[l]))
        print(ans) 
        ```

        - 이런 상황에서 n을 하나 줄일 때 도움이 되는 투포인터
        - 완전 탐색 N^4 는 불가능
        - N^3 이면 가능할 듯
        - 이러한 경우에 투 포인터 사용
    - 투 포인터

        ```python
        
        n = int(input())
        ls = sorted(map(int, input().split()))
        
        ans = int(1e10)
        # 두 눈사람의 높이 차가 0이될 때가 최소임 -> 이때는 그냥 바로 반복문 탈출할 수 있도록
        flags = False
        
        for i in range(n-3):
          for j in range(i+3, n):
            s = i + 1
            e = j - 1
            while s < e:
              ans = min(ans, abs(ls[i] + ls[j] - (ls[s] + ls[e])))
        
              if ans == 0 :
                flags = True
                break
              if ls[i] + ls[j] < ls[s] + ls[e]:
                e -= 1
        
              else :
                s += 1
        
        print(ans)
        ```


### 조건을 만족하는 연속된 구간

- 백준 2003번 수들의 합2
    - 완전 탐색

        ```python
        for i in range(n):
        	total = 0
        	for j in range(i,n):
        		total += ls[j]
        		if total == m:
        			cnt += 1
        		
        		if total > m:
        			break
        ```

    - 투 포인터
        - s =0 , e = 0
        - e < n : 정상적인 구간에서 반복을 진행하겠다
        - e += 1 : 구간을 늘린다.  s += 1 : 구간을 줄인다

        ```python
        r = -1
        total = 0
        ans = 0
        # r은 e(end_point)의 역할 l은 s(start_point)의 역할
        for l in range(n):
          while r + 1 < n  and total < m:
            r += 1
            total += ls[r]
          if total == m:
            ans += 1
          total -= ls[l]
        ```