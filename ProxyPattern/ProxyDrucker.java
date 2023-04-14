package ProxyPattern;

public class ProxyDrucker {

    private Drucker drucker;

    public ProxyDrucker(){
        this.drucker = new ColourDrucker();
    }

    public void drucken(String text){
        this.drucker.drucken(text);
    }

    public void switchTo(Drucker newDrucker){
        this.drucker = newDrucker;
    }
    
}
