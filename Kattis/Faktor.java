import java.util.Scanner;
class Faktor{
	public static void main(String[] args){
		Scanner s = new Scanner(System.in);
		int a = s.nextInt();
		int i = s.nextInt();
		int m = a * (i - 1) + 1;
		System.out.println(m);
	}
}
