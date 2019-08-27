#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include"cJSON.h"
/*
创建一个如下的json文件:

{
        "country":      "china",
        "stars":        [{
                        "name": "Faye",
                        "address":      "beijing"
                }, {
                        "name": "andy",
                        "address":      "HK"
                }, {
                        "name": "eddie",
                        "address":      "TaiWan"
                }]
}


*/
int main(void)
{
    //先创建空对象
    cJSON *json = cJSON_CreateObject();
    //在对象上添加键值对
    cJSON_AddStringToObject(json,"country","china");
    //添加数组
    cJSON *array = NULL;
    cJSON_AddItemToObject(json,"stars",array=cJSON_CreateArray());
    //在数组上添加对象
    cJSON *obj = NULL;
    cJSON_AddItemToArray(array,obj=cJSON_CreateObject());
    cJSON_AddItemToObject(obj,"name",cJSON_CreateString("Faye"));
    cJSON_AddStringToObject(obj,"address","beijing");
    //在对象上添加键值对
    cJSON_AddItemToArray(array,obj=cJSON_CreateObject());
    cJSON_AddItemToObject(obj,"name",cJSON_CreateString("andy"));
    cJSON_AddItemToObject(obj,"address",cJSON_CreateString("HK"));
    
    cJSON_AddItemToArray(array,obj=cJSON_CreateObject());
    cJSON_AddStringToObject(obj,"name","eddie");
    cJSON_AddStringToObject(obj,"address","TaiWan");
    
    //清理工作
    FILE *fp = fopen("4create.json","w");
    char *buf = cJSON_Print(json);
    fwrite(buf,strlen(buf),1,fp);
    fclose(fp);
    cJSON_Delete(json);
    return 0;
}
