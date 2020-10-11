class Parentheses_Balance{

    public static void main(final String[] args) {
        final java.util.Scanner sc = new java.util.Scanner(System.in);
        final int n = sc.nextInt();
        for(int i = 0; i < n; i++){
            String s = sc.next();
            while(s.contains("()") || s.contains("[]")){
                s = s.replace("()", "");
                s = s.replace("[]", "");
            }
            if(s.length() > 0)System.out.println("No");
            else System.out.println("Yes");
        }
        sc.close();
    }
}