public class Cetiri
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int a = sc.nextInt(), b = sc.nextInt(), c = sc.nextInt();
        int[] nums = new int[3];
        nums[0] = Math.min(a, Math.min(b, c));
        nums[2] = Math.max(a, Math.max(b, c));
        if(a != nums[0] && a != nums[2])nums[1] = a;
        else if(b != nums[0] && b != nums[2])nums[1] = b;
        else nums[1] = c;
        int abs = Math.min(nums[1] - nums[0], nums[2] - nums[1]);
        boolean bab = abs == nums[1] - nums[0], bbc = abs == nums[2] - nums[1];
        if(bab && bbc){
            System.out.println(nums[2] + abs);
        }else{
            if(bab){
                System.out.println(nums[1] + abs);
            }else{
                System.out.println(nums[0] + abs);
            }
        }
    }
}
