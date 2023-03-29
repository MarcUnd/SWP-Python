package ObserverPattern;

public class TempSensor extends Sensor{
    
    private Data currentData;

    public void setCurrentData(Data data, boolean push){
        this.currentData = data;
        if(push){
            sendDataPush(data);
        }else{
            sendDataPull(this);
        }
        
    }

    public Data getCurrentData(){
        return this.currentData;
    }
}
