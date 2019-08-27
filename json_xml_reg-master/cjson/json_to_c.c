#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include"cJSON.h"
/*
 *  从json字符串数据:
     "{\"family\":[\"father\",\"mother\",\"brother\",\"sister\",\"somebody\"]}";
 *  提取c的数据结构
 *
 * */

int main(void)
{
    char *string = "{\"family\":[\"father\",\"mother\",\"brother\",\"sister\",\"somebody\"]}";
    //从缓冲区中解析出JSON结构
    cJSON *json = cJSON_Parse(string);
    cJSON *node = NULL;

    //cJOSN_GetObjectItem 根据key来查找json节点, 如果有返回一个node结构,后面通过node(key)会得到value
    printf("stirng = %s\n",string );
    node = cJSON_GetObjectItem(json,"family");
    if(node == NULL)
    {
        printf("family node == NULL\n");
    }
    else
    {
        printf("found family node\n");
    }

    if(node->type == cJSON_Array)
    {
        printf("array size is %d\n",cJSON_GetArraySize(node));
    }
    //非array类型的node 被当做array获取size的大小是未定义的行为 不要使用
    cJSON *tnode = NULL;
    int size = cJSON_GetArraySize(node);
    int i;

// 遍历json中数据的第一种方法
    for(i=0;i<size;i++)
    {
        tnode = cJSON_GetArrayItem(node,i);
        if(tnode->type == cJSON_String)
        {
            printf("value[%d]:%s\n",i,tnode->valuestring);
        }
        else
        {
            printf("node' type is not string\n");
        }
    }

// 遍历json中数据的第二种方法
    cJSON_ArrayForEach(tnode,node)
    {
        if(tnode->type == cJSON_String)
        {
            printf("int forEach: vale:%s\n",tnode->valuestring);    
        }
        else
        {
            printf("node's type is not string\n");
        }
    }
    return 0;
}
