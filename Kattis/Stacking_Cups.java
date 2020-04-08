public class Cups
{
    public static void main(String[] args){
        java.util.Scanner sc = new java.util.Scanner(System.in);
        int n = sc.nextInt();
        String[] cups = new String[n];
        int[] colors = new int[n];
        for(int i = 0; i < n; i++){
            String f = sc.next();
            String s = sc.next();
            int d;
            if(Character.isDigit(f.charAt(0))){
                d = Integer.parseInt(f) / 2;
                cups[i] = s;
            }else{
                d = Integer.parseInt(s);
                cups[i] = f;
            }
            colors[i] = d;
        }
        for(int i = 0; i < n; i++){
            for(int j = i; j < n; j++){
                if(colors[i] > colors[j]){
                    int temp = colors[i];  String t = cups[i];
                    colors[i] = colors[j]; cups[i] = cups[j];
                    colors[j] = temp;      cups[j] = t;
                }
            }
        }
        for(int i = 0; i < n; i++){
            System.out.println(cups[i]);
        }
    }
}
