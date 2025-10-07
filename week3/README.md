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
사용자가 무언가 입력했을 때 맞다 틀리다 결과를 출력하는 코드로 추정


그럼 if문에서 정답과 입력 답을 비교해서 여부를 판단할 것으로 생각

**sub_140001000** 더블 클릭!


```
_BOOL8 __fastcall sub_140001000(const char *a1)
{
  return strcmp(a1, "Compar3_the_str1ng") == 0;
}
```
변수 a1과 "Compar3_the_str1ng"을 비교한 결과를 return하는 코드

변수 a1은 사용자 입력 변수인 것 같고 정답은 **"Compar3_the_str1ng"**

![업로드 실패](https://github.com/ramm113/EVISION_8TH/blob/main/week3/%EB%93%9C%EB%A6%BC%ED%95%B5%20%EC%84%B1%EA%B3%B5%20%ED%99%94%EB%A9%B4.png)


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
  unsigned int v1; // [esp+1Ch] [ebp-4h] BYREF    #사용자 입력 변수 v1을 unsigned int로 선언해 0 미만을 고려할 필요 없음

  __main();
  while ( 1 )
  {
    printf("Enter an integer (within two digits): ");
    scanf("%d", &v1);
    if ( v1 < 0x64 )    #!의사코드에선 100을 16진수로 표현
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

가장 크게 두 가지의 차이를 발견
1. 사용자 입력값을 받을 변수를 애초에 unsigned int로 설정해 더 효율적
2. 10진수가 아닌 16진수를 사용함

복잡하지 않은 코드라 그런지 직접 입력한 코드와 의사코드가 상당히 유사함을 알 수 있다
