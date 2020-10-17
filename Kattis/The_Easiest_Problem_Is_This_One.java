import java.util.Scanner;
class The_Easiest_Problem_Is_This_One
{
	static int sum(int n){
		int sum = 0;
		while(n != 0){sum += n % 10; n /= 10;}
		return sum;
	}

	static int min(int n){
		int sum = sum(n);
		for(int i = 11; ; i++){
			if(sum(n * i) == sum)return i;
		}
	}

	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		while(true){
			int n = sc.nextInt();
			if(n == 0)break;
			System.out.println(min(n));
		}
		sc.close();
	}
}
