public class Star_Arrangements
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int stars = sc.nextInt();
        System.out.println(stars + ":");
        for(int i = 2; i < stars; i++){
            for(int j = i - 1; j <= i; j++){
                int d = 2;
                while(true){
                    int sum = 0;
                    if(d % 2 == 0){
                        sum += i * (d / 2);
                        sum += j * (d / 2);
                    }else{
                        sum += i * ((d / 2) + 1);
                        sum += j * (d / 2);
                    }
                    if(sum == stars){System.out.println(i + "," + j); break;}
                    else if(sum < stars)d++;
                    else break;
                }
            }
        }
    }
}
