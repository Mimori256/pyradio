#include <stdio.h>
#include <string.h>
#include <time.h>

int main(void){

    char str[256];
    char cnp[]="-=";
    char *tmp;
    char *name;
    char *mname;

    char time_color[] = "\033[32m";
    char artist_color[] = "\033[34m";
    char title_color[] = "\033[34m";

    int  slengs;

    float cnt=0;

    time_t now;
    struct tm *ntime;

    while(1){
    fgets(str,sizeof(str),stdin);

            if(str[0]=='I'){

        tmp=strtok(str,"'");          
        name=strtok(NULL,"-");          
        mname=strtok(NULL,";");         
        mname+=1;                       
        slengs=strlen(mname);           
        mname[slengs-1]='\0';           

        printf("\n");

        time(&now);
        ntime = localtime(&now);

        printf("%s%2d/%2d  %02d:%02d\033[0m\n",time_color,ntime->tm_mon+1,ntime->tm_mday,ntime->tm_hour,ntime->tm_min);

        printf("%sARTIST- \033[0m%s\n",artist_color,name);
        printf("%sMUSIC-- \033[0m%s\n",title_color,mname);
        cnt=0;
        } 
    }
}
