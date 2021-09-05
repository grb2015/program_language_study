
/**
 * Learn Java from https://www.liaoxuefeng.com/
 * 
 * @author liaoxuefeng  
 * 
 * rbg added : 演示如何将代码分布在不同的文件中。
 */
public class Main {

	public static void main(String[] args) {
		Person p = new Person("小明", 12);
		Student s = new Student("小红", 20, 99);
		System.out.println(p.getAge());
		System.out.println(s.getAge());
		System.out.println("哈哈");
	}

}
