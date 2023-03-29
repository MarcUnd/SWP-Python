package ObserverPattern;

public class Client {
    public static void main(String args[]){
        TempSensor sens = new TempSensor();
        BigScreen biggy = new BigScreen();

        sens.addSub(new Screen());
        sens.addSub(biggy);

        sens.setCurrentData(new Data(25.73), true);

        sens.remSub(biggy);

        sens.setCurrentData(new Data(24.93), false);
        
    }
}
