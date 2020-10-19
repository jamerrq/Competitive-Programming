public class Doorman
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int n = sc.nextInt();
        String queue = sc.next();
        int count = 0;
        int in = 0;
        for(int i = 0; i < queue.length(); i++){
            if(queue.charAt(i) == 'W'){
                if(in + 1 > n){
                    if(i == queue.length() - 1 ||
                       queue.charAt(i + 1) == queue.charAt(i)){
                        break;
                    }else{
                        queue = queue.substring(0,i) + "MW" +
                        queue.substring(i + 2);
                    }
                }
            }else{
                if(in - 1 < -n){
                    if(i == queue.length() - 1 ||
                    queue.charAt(i + 1) == queue.charAt(i)){
                        break;
                    }else{
                        queue = queue.substring(0,i) + "WM" +
                        queue.substring(i + 2);
                    }
                }
            }
            char c = queue.charAt(i);
            if(c == 'W')in++;
            else in--;
            count++;
        }
        System.out.println(count);
        sc.close();
    }
}
