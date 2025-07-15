### Git reset과 revert의 차이
- revert (돌아간다)
    - 특정 커밋을 삭제하는 명령어
    - 삭제한 기록이 커밋에 남은
    - 예시
    
    ```bash
    > git log --oneline
    ab54f4d c
    **12e95a1** b
    7e33ce9 a
    
    > git revert 12e95a1
    [main d557580] Revert "b"
     1 file changed, 0 insertions(+), 0 deletions(-)
     delete mode 100644 b
     
    > git log --oneline
    **d557580 (HEAD -> main) Revert "b"**
    ab54f4d c
    12e95a1 b
    7e33ce9 a
    ```
    
    - b 커밋 내용 부분만 삭제 되고 마지막 커밋에 기록됨.
- reset
    - 해당 커밋을 삭제하는 것은 revert와 같음
    - 다른 점은 삭제한 기록이 남지 않고 아예 커밋을 삭제
    - 예시
    
    ```bash
    git reset --soft HEAD~1
    ```
    
    - 마지막 커밋을 삭제하고 마지막 커밋 코드의 내용을 **스테이징 영역**에 올림.
    
    ```bash
    git reset --mixed HEAD~1
    ```
    
    - 마지막 커밋을 삭제하고 마지막 커밋 코드의 내용을 **작업 영역**으로 복구
    
    ```bash
    git reset --hard HEAD~1
    ```
    
    - 커밋도 삭제하고 내용도 삭제! (위험함으로 권장하지는 않음)

### reset과 revert의 차이점과 협업시 revert를 추천하는 이유

- 만약 이미 리모트(Github)에 올라가 있는 커밋을 reset을 하면 해당 커밋이 아예 사라진다.
- 다른 작업자도 해당 커밋을 가지고 있기 때문에 reset을 하고 다른 작업을 해서 다시 리모트에 코드를 올리면 충돌이 일어난다.
- **반면 revert의 경우는 이전에 커밋 기록은 그래도 있고 취소 했다는 커밋이 새롭게 생성되기 때문에 충돌도 나지 않고 히스토리를 남겨서 다른 작업자들도 알 수 있게 된다.**
-