**과제 1 : 드림핵 기초 문제 풀이**
먼저 ida에서 파일을 열고 쉬운 해석을 위해 F5로 의사코드로 만들기..
```
int __fastcall main(int argc, const char **argv, const char **envp)
{
  char v4[256]; // [rsp+20h] [rbp-118h] BYREF

  memset(v4, 0, sizeof(v4));
  sub_140001190("Input : ", argv, envp);
  sub_1400011F0("%256s", v4);
  if ( (unsigned int)sub_140001000(v4) )
    puts("Correct");
  else
    puts("Wrong");
  return 0;
}
```
무언가 입력했을 때 맞다 틀리다 결과를 출력하는 코드로 추정
그럼 if문에서 정답과 입력 답을 비교해서 여부를 판단하겠지..?
sub_140001000 더블클릭!
```
_BOOL8 __fastcall sub_140001000(const char *a1)
{
  return strcmp(a1, "Compar3_the_str1ng") == 0;
}
```
a1은 사용자 입력 변수인 것 같고 정답은 "Compar3_the_str1ng"
![업로드 실패]()

**과제 2 : 직접 C언어 exe 파일을 빌드한 후, ida로 열어 의사 코드와 비교**

직접 입력한 코드
```markdown
```C
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int KEYWORD = 13;

int main(){
    int num;

    while (1){
        printf("Enter an integer (within two digits): ");
        scanf("%d", &num);

        if (num > 99 || num < 0){
        printf("Enter again.\n");
        }
        else{
            break;
        }
    }

    if(num == KEYWORD){
        printf("Right!");
    } else {
        printf("Wrong..");
    }
    return 0;
}
```

의사코드
```markdown
int main()
{
  unsigned int v1; // [esp+1Ch] [ebp-4h] BYREF

  __main();
  while ( 1 )
  {
    printf("Enter an integer (within two digits): ");
    scanf("%d", &v1);
    if ( v1 < 0x64 )    #!의사코드에선 16진수로 표현, 0 이하 조건은 없어짐!
      break;
    puts("Enter again.");
  }
  if ( v1 == KEYWORD )
    printf("Right!");
  else
    printf("Wrong..");
  return 0;
}
```

