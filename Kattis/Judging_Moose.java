public class Judging_Moose
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int left = sc.nextInt();
        int right = sc.nextInt();
        if(left == 0 && right == 0)System.out.println("Not a moose");
        else{
            int n = Math.max(left, right) * 2;
            if(left == right){
                System.out.println("Even " + n);
            }else{
                System.out.println("Odd " + n);
            }
        }
        sc.close();
    }
}
