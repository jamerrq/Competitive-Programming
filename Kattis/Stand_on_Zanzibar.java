import java.util.Scanner;
import java.util.ArrayList;
class Stand_on_Zanzibar{
	public static void main(String[] args){
		Scanner s = new Scanner(System.in);
		int n = s.nextInt();
		for(int i = 0; i < n; i++){
			ArrayList<Integer> ts = new ArrayList<>();
			while(true){
				int t = s.nextInt();
				if(t == 0)break;
				ts.add(t);
			}
			int e = 0;
			for(int j = 1; j < ts.size(); j++){
				if(ts.get(j) > ts.get(j-1)*2){
					e += ts.get(j) - ts.get(j - 1)*2;
				}
			}
			System.out.println(e);
		}
		s.close();
	}
}
