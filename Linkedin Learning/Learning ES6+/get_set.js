let attendance = {
    _list: [],
    set addName(name) {
        this._list.push(name);
    },
    get list() {
        return this._list.join(", ");
    }
};

attendance.addName = "Shyam Sharma"
attendance.addName = "Bade Bahadur"

console.log(attendance.list);
