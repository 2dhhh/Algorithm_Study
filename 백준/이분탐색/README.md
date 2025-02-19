### 이분 탐색

- 이분 탐색은 업다운 게임임
    - 소주병 병뚜껑 숫자 맞추기 게임(업 다운 게임)
    - 1~50 을 고르라면 대부분이 25부터 부른다
    - 25 down → 13 up → 19 down → 16 find 와 같은 과정을 거친다
- 정답으로 가능한 범위를 줄여가는 것 → 이분 탐색은 절반씩 범위를 줄여가는 것
- 이분 탐색 아이디어
    - 후보 범위가 [s, e]
    - mid 값을 봤을 때 후보 절반을 날릴 수 있다면 이분 탐색이 가능
    - 정렬된 배열에서 특정 수가 존재하는지 혹은 특정 수의 인덱스 찾기는 이분 탐색으로 풀 수 있는 수 많은 가지 중 하나
    - 정답 후보 구간에서 답이 될 수 없는 구간을 날린다 → 정답의 후보를 줄여나가기
- 시간 복잡도 : O(logN)
- 이분 탐색 응용
- 예시 1
    - 문자열이 주어진다
    - xxxxxxxxxxxxxoooooo
    - 이 o 중에 제일 왼쪽의 index가 무엇인가?
    - 이분 탐색이다

        ```python
        xxxxxxxxxxxxxoooooo
        s
                          e
        ```

    - 우리는 이 문자열의 단조성을 알고 있다 (x만 나오다가 o가 나옴)
    - 가운데 찍었는데 만약 x다
        - 뭘 알 수 있을까?
        - 가운데 포함 왼쪽은 전부 x다 → 범위를 줄일 수 있다

        ```python
        xxxxxxxxxxxxxoooooo
                 s
                          e
                          
                                            
        xxxxxxxxxxxxxoooooo
                 s 
                       e 
        ```

    - 가운데가 이제 o면 우선 답에 저장을 해둔다
    - ans = 가운데 값

        ```python
        xxxxxxxxxxxxxoooooo
                     s 
                     e 
        ```

    - 코드

        ```python
        mid = s + e // 2
        
        if arr[mid] == 'x':
        	s = mid + 1
        	
        else : 
        	ans = mid
        	e = mid - 1 
        ```

- 예시 2
    - xxxxxxxxxxxooooooooooo!!!!!!!!!@@@@@@@@@@
    - ! 중에 제일 오른쪽 인덱스 찾고 싶음
    - mid
        - x인 경우 → s = mid + 1 : mid도 답이 아니고 그 왼쪽도 답이 아님
        - o인 경우 → o = mid + 1 : mid도 답이 아니고 그 왼쪽도 답이 아님
        - !인경우 → ans = mid , s = mid + 1 : 정답의 후보, 후보 왼쪽은 정답이 아님
        - @인경우 → e = mid - 1 : mid도 답이 아니고, 그 오른쪽도 답이 아님

### 대표 문제

- 백준 10815번 숫자 카드

    ```python
    for num in ls_m:
      ans = False
      s ,e = 0, n-1
      
      while s <= e :
        mid = (s + e) // 2
        if ls_n[mid] == num:
          ans = True
          break
    
        elif ls_n[mid] > num:
          e = mid -1
    
        else :
          s = mid + 1
    
      if ans:
        print(1, end =" ")
      else :
        print(0, end = " ")
    ```


- 백준 10816번 숫자 카드 2

```python
for num in ls_m:
  s, e = 0, n-1
  l = -1
  # num을 만족하는 수에서 가장 왼쪽 인덱스 구하기
  while s <= e:
    mid = (s+e) // 2
    if ls_n[mid] == num :
      l = mid
      e = mid -1

    elif ls_n[mid] > num :
      e = mid -1
    else :
      s = mid + 1

  s,e = 0, n-1
  r = -1
  # num을 만족하는 수에서 가장 오른쪽 인덱스 구하기
  while s <= e:
    mid = (s+e) // 2
    if ls_n[mid] == num:
      r = mid
      s = mid + 1
    elif ls_n[mid] < num:
      s = mid + 1
    else :
      e = mid - 1

  if r == -1 or l == -1:
    print(0, end =" ")
  else :
    print(r-l+1, end = " ")
```

- 백준 2805번 나무자르기
    - 매개변수 탐색 (Parametric Search)

        <aside>
        ✅

      매개변수 탐색은 조건을 만족하는 최댓값을 구할 때 사용할 수 있는 탐색 방법이다.
      매개변수 탐색은 이분 탐색으로 최종 답안에 가까워져 가는 방식으로 문제를 해결한다. 이분 탐색의 mid 값이 바로 정답이 되지는 않지만, 정답이 될 수 있는지 없는지 여부는 판단할 수 있다

        </aside>

    - 완전 탐색 풀이 : 모든 높이에서 전부 잘라보기 → 이 행위 자체가 매개변수 탐색임
    - 적어도 M미터의 나무를 가져가기 위해 절단기의 최대 높이는?
    - 동치 → 절단기 높이를 x로 했을 때 적어도 M미터를 가져갈 수 있는가?
    - 매개변수 탐색 형태가 단조성을 띈다 → 이분 탐색 가능

    - 정리
        - 완전 탐색부터 떠올리기
        - O, X 형태 → 매개변수 탐색 + 이분 탐색
        - 매개 변수 탐색 + 이분탐색 키워드
            - 최대값을 최소로, 최소값을 최대로 → 거의 100%
                - 정답의 후보에서 답을 찾아가는 과정임