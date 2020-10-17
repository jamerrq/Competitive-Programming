public class Roaming_Romans{
  public static void main(String[] args){
    java.util.Scanner sc = new java.util.Scanner(System.in);
    double em = sc.nextDouble();
    double rm = em * 1000 * (double)(5280.0 / 4854.0);
    double df = rm - (int)(rm);
    if(df >= 0.5){
      System.out.println((int)(rm + 1));
    }else{
      System.out.println((int)rm);
    }
    sc.close();
  }
}
