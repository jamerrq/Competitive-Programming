public class Ants{
	static int cross(int a, int b, int l, int t){
		if(a <= 0 && b >= l)return t;
		if(a == b + 1)return cross(b, a, l, t + 1);
		return cross(a - 1, b + 1, l, t + 1);
	}

	public static void main(String[] args){
		java.util.Scanner sc = new java.util.Scanner(System.in);
		int cs = sc.nextInt();
		for(int i = 0; i < cs; i++){
			int l = sc.nextInt(), n = sc.nextInt();
			int min = l, max = 0, mid = l;
			for(int j = 0; j < n; j++){
				int a = sc.nextInt();
				if(a > max)max = a;
				if(a < min)min = a;
				if(Math.abs(l / 2 - a) < Math.abs(l / 2 - mid))mid = a;
			}
			int tmax = cross(max, min, l, 0);
			System.out.println(Math.min(Math.abs(l - mid), mid) + " " + tmax);
		}
	}
}