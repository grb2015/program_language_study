/*
* @file 	:	Puppy.java
* @brief	:	构造函数
* @histroy	:   2017-06-25 16:33:51  renbin.guo created
* @note		:
* @usage	:
*/


/**
 * 	定义一个public 的Puppy类
 */
public class SuShu{

    /*类的构造函数*/
    public int  isSuShu(int n ){
      for(int i = 2 ; i < n-1 ; i++){
          if (n % i == 0){
            //   System.out.printf(" %d不是素数.",n);
              return 1;
          }
      }
      System.out.printf(" %d是素数.\n",n);
      return 0;
   }

 
 	 /*类的成员函数--主函数（进行测试）*/
   public static void main(String []args){
      SuShu s = new SuShu();
      for(int i = 1; i<101 ; i++){
         s.isSuShu( i );
      }
   }
}