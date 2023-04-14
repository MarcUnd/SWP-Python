package ProxyPattern;

public class Main {

    public static void main(String args[]){
        ProxyDrucker meinDrucker = new ProxyDrucker();

        meinDrucker.drucken("This text was written using many colours");

        meinDrucker.switchTo(new SWDrucker());

        meinDrucker.drucken("This text was written using no colours");
    }
    
}
