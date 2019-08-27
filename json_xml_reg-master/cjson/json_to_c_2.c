#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>
#include"cJSON.h"
/*
 *从json文件6-2.json中读取数据进行解析让C中使用
 *
 * 6-2.json
{
    "name": "Jack (\"Bee\") Nimble",
    "format": {
        "type":       "rect",
        "width":      1920,
        "height":     1080,
        "interlace":  false,
        "frame rate": 24
    }
}

*/
int main(int argc, char const *argv[])
{

    int fd;
    char read_buf[500];
    int len = -1 ;
    int i ;
    fd = open("6-2.json",O_RDWR);
    len = read(fd,read_buf,500);
    read_buf[len] = '\0';

    char *my_json_string = read_buf;
    printf("my_json_string = %s\n",my_json_string );

	/* code */
	cJSON * root = cJSON_Parse(my_json_string);

	/*test 1*/
	cJSON *format = cJSON_GetObjectItemCaseSensitive(root, "format");
	cJSON *framerate_item = cJSON_GetObjectItemCaseSensitive(format, "frame rate");
	double framerate = 0;
	if (cJSON_IsNumber(framerate_item))
	{
		  framerate = framerate_item->valuedouble;
		  printf("%f\n",framerate );
	}
	cJSON_SetNumberValue(framerate_item, 25);        //modify the frame rate value;


	/*test 2*/
	cJSON * name = cJSON_GetObjectItemCaseSensitive(root,"name");
	printf("name = %s\n",name->valuestring );
	return 0;
}
