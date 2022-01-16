function skier(name, sound) {
    return {
        //without object literals, we declare values in objects as below:
        //name: name, 
        //sound: sound,

        //with object literals
        name, 
        sound, 
        powderYell: function () {
            let yell = this.sound.toUpperCase();
            console.log(`${yell}! ${yell}!`);
        }
    };
}

skier("Sendy", "woo").powderYell();