class RandomizedSet {
    HashMap<Integer,Integer> map;
    public RandomizedSet() {
        map=new HashMap<>();
    }
    
    public boolean insert(int val) {
        if(map.containsKey(val)){
            return false;
        }
        map.put(val,1);
        return true;
    }
    
    public boolean remove(int val) {
        if(map.containsKey(val)){
            map.remove(val);
            return true;
        }
        return false;
    }
    
    public int getRandom() {
        List<Integer> keysAsArray = new ArrayList<Integer>(map.keySet());
        Random r = new Random();
        return keysAsArray.get(r.nextInt(keysAsArray.size()));
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
