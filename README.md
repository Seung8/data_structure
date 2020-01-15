### 자료구조 알고리즘

패스트캠퍼스 온라인 강의 수강 기록입니다.



### 스택(Stack)

- LIFO(Last-In, First-Out): 나중에 들어온 데이터가 먼저 나감

- 용어:
  - push: 데이터 넣기
  - pop: 데이터 꺼내기
- 대표적으로 재귀함수 프로세스 스택에서 사용
- [예제 코드](/stack)


### 큐(Queue)

- FIFO(First-In, First-Out): 먼저 들어온 데이터가 먼저 나감

- 용어:
  - Enqueue: 데이터 넣기
  - Dequeue: 데이터 꺼내기
- [Python queue 라이브러리](https://docs.python.org/ko/3/library/asyncio-queue.html)를 통해 구현 가능
  - Queue.put(): 데이터 넣기
  - Queue.get(): 데이터 꺼내기
  - Queue.qsize(): Queue 데이터 개수 반환
  - Queue.queue: 전체 큐 항목 반환 print(list(Queue.queue)) 처럼 사용
- 대표적으로 스케쥴링 작업에 사용(작업 목록을 순차적으로 저장 후, 먼저 저장한 작업부터 처리)
- [예제 코드](/queue)