### 누적 합(Prefix Sum)

- 가장 자주 출제되는 주제 중 하나임
- 수열과 쿼리 문제를 다룬다
    - 수열이 주어지고, 다음에 쿼리를 수행하는 프로그램이
- 반드시 합(sum)일 필요가 없음 → (백준)창고 다각형 문제
    - 왼쪽 오른쪽을 명확하게 표현하는 것이 중요하다.
        - prefix_sum
        - suffix_sum
        - prefix_max
        - prefix_min
        - 어떤 역할의 리스트인지 명시할 것

        ```python
        """ 창고다각형 예시 """
        prefix_max = [] # 1 ~ i 번째 위치 중 최대 높이
        suffix_max = [] # i ~ n 번째 위치 중 최대 높이
        
        # prefix는 왼쪽
        # suffix는 오른쪽 
        """
        [주의점]
        suffix를 구할 때 배열 인덱스 크기 설정 주의 
        그냥 누적 합과 동일하게 설정하면 인덱스 범위 예외 터트림
        """
        ```

- 배열(수열)의 1번 위치부터 값을 저장하고 누적 합을 구함
    - 누적 합 배열 이용할 때는 인덱스 1번부터 하는게 유용
    - 배열에 필요없는 0과 같은 수 집어넣기
        - 기본적인 누적합 구하는 방법 → 일차원 누적합

            ```python
            """기본적인 누적합 구하는 방법"""
            import sys 
            
            input = sys.stdin.readline
            
            n, m = map(int, input().split())
            
            ls = [0] + list(map(int, input().split()))
            
            prefix_sum = [0] * (n+1)
            
            for i in range(1, n+1):
            	prefix_sum[i] = prefix_sum[i-1] + ls[i]
            
            for _ in range(m):
            	a, b = map(int, input().split())
            	print(prefix_sum[b] - prefix_sum[a-1]
            	
            	
            """
            arr      0 5 4 3 2 1
            
            prefix_sum    0 5 9 12 14 15
            
            prefix_sum[i] := 1번부터 i 번째 수까지 합
            """
            
            ```

- 누적 합을 사용하는 이유 : 구간 get 쿼리를 점 get 으로 전환할 수 있다
- i번째 ~ j번째 구간의 합 : prefix_sum[j] - prefix_sum[i-1]
- 이차원 누적 합
    - 이차원 누적합을 이용한 구간 합 구하는 방법
        - prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]
        - m(x1, y1)에서 n(x2, y2)까지 구간 합
            - prefix_2d_sum[x2][y2] - prefix_2d_sum[x2][y1-1] - prefix_2d_sum[x1-1][y2] + prefix_2d_sum[x1-1][y1-1]
        - [참고]

          [누적 합(prefix sum), 2차원 누적합(prefix sum of matrix) with java](https://nahwasa.com/entry/%EB%88%84%EC%A0%81-%ED%95%A9prefix-sum-2%EC%B0%A8%EC%9B%90-%EB%88%84%EC%A0%81%ED%95%A9prefix-sum-of-matrix-with-java#2%EC%B0%A8%EC%9B%90_%EB%88%84%EC%A0%81_%ED%95%A9_(prefix_sum_of_matrix))

        - 이차원 누적 합 및 구간 합 예제

            ```python
            
            """ 구간 합 구하기 5 """
            import sys
            
            input = sys.stdin.readline
            
            n, m = map(int, input().split())
            
            ls = [list(map(int, input().split())) for _ in range(n)]
            prefix_2d_sum = [[0]*(n+1) for _ in range(n+1)]
            
            for i in range(1, n+1):
              for j in range(1,n+1):
                prefix_2d_sum[i][j] = prefix_2d_sum[i-1][j] + prefix_2d_sum[i][j-1] - prefix_2d_sum[i-1][j-1] + ls[i-1][j-1]
            
            for _ in range(m):
              x1, y1, x2, y2 = map(int, input().split())
              print(prefix_2d_sum[x2][y2] - prefix_2d_sum[x1-1][y2] - prefix_2d_sum[x2][y1-1] + prefix_2d_sum[x1-1][y1-1])
            
            ```


### 쿼리 란?

- ~~오프라인 쿼리 → 알 필요가 없음(알고리즘 문제에 출제되지 않는다)~~
- 온라인 쿼리
    - 질문이 들어오는 즉시 대답하는 것을 말한다
    - update
        - 점 update : a[i]를 x로 바꿔라, a[i] 에 3을 더해라
        - 구간 update : a[i] ~  a[j]까지 모두 3으로 바꿔라 or 3을 더해라
    - get
        - 점 get : a[i] 를 출력해라
        - 구간 get : a[i] ~ a[j]까지의 합(구간 합), 최대 공약수, xor, k보다 큰 값들의 개수

## 문제 유형

### 1. update가 없고 get 만 있는 경우

1. [백준_2559] 수열 → 단순 구간 합을 이용

```python
"""
[수열]

연속적인 며칠 동안의 온도 합이 최대가 되는지 구하는 문제

수열의 연속 합 := 수열의 구간합을 구하는 문제

구간 합은 점 get 으로 전환해서 풀수있다 

"""
```

1. [백준_2304] 창고 다각형
- 누적 합을 응용해서 해결할 수 있다
- 반드시 합을 사용하지 않아도 되는 경우이다

```python
import sys

input = sys.stdin.readline

n = int(input())
ls = [0] * 1001
prefix_max = [0] * 1111
suffix_max = [0] * 1111

for _ in range(n):
  a, b = map(int, input().split())
  ls[a] = b

ans = 0
for i in range(1, 1001):
  prefix_max[i] = max(prefix_max[i-1], ls[i])

for i in range(1001)[::-1]:
  suffix_max[i] = max(suffix_max[i+1], ls[i])

for i in range(1001):
  ans += min(prefix_max[i], suffix_max[i])

print(ans)

```

### 2. update가 모두 일어난 후 마지막에 get 하는 경우

- imos 정리하기

### 예시

1. [백준_3020] 개똥 벌레