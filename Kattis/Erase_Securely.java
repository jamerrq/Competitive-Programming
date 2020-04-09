public class Erase_Securely{
	public static void main(String[] args){
		java.util.Scanner sc = new java.util.Scanner(System.in);
		int n = sc.nextInt();
		String before = sc.next();
		String after = sc.next();
		String e = "";
		for(int i = 0; i < before.length(); i++){
			if(before.charAt(i) == after.charAt(i)){
				e += 2;
			}else{
				e += 1;
			}
		}
		if(e.indexOf("1") != -1 && e.indexOf("2") != -1){
			System.out.println("Deletion failed");
		}else{
			System.out.println("Deletion succeeded");
		}
	}
}
