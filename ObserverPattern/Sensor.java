package ObserverPattern;

import java.util.ArrayList;

public abstract class Sensor {
    
    public ArrayList<Subscriber> subs = new ArrayList<Subscriber>();

    public void addSub(Subscriber sub){
        subs.add(sub);
    }

    public void remSub(Subscriber sub){
        subs.remove(sub);
    }

    public void sendDataPush(Data data){
        for(Subscriber s : subs){
            s.getData(data);
        }
    }

    public void sendDataPull(Sensor sens){
        for(Subscriber s : subs){
            s.getDataFromSensor(sens);
        }
    }

    public Data getCurrentData(){
        return null;
    }
}
