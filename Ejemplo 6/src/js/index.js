let songs = [
    {
        title: "AUKAAT  Rahim Pardesi",
        url: "C:/Users/soulo/Desktop/EjemplosIPC2/Ejemplo 6/src/songs/",
        ext: ".mp3",
        img: "https://los40.com/los40/imagenes/2017/11/28/album/1511885438_220718_1512040978_album_normal.jpg"
    },
    {
        title: "BLACKBEAR - HOT GIRL BUMMER",
        url: "C:/Users/soulo/Desktop/EjemplosIPC2/Ejemplo 6/src/songs/",
        ext: ".wav",
        img: "https://i.pinimg.com/originals/83/9c/f5/839cf5dafaa9a95d9fdfb5e91f2b20da.jpg"
    },
    {
        title: "touch the sky",
        url: "C:/Users/soulo/Desktop/EjemplosIPC2/Ejemplo 6/src/songs/",
        ext: ".mp3",
        img: "https://edit.org/images/cat/caratulas-cd-big-2019090615.jpg"
    }
]

let actual = 0;
let statusSong = false;
let music; // new Audio();

let title = document.getElementById("title-song");
let cover = document.getElementById("cover");
let ctlTime = document.getElementById("ctlTime");
let progressBar = document.getElementById("progressBar");
let next = document.getElementById("btn-next");
let play = document.getElementById("btn-play");
let last = document.getElementById("btn-last");

let convetSeconds = (seconds) =>{
    return new Date(seconds*1000).toISOString().substr(11,8);
}

let setEventListeners = (musicObject) => {
    music.ontimeupdate = () =>{
        ctlTime.innerHTML = convetSeconds(musicObject.currentTime) + "/" + convetSeconds(musicObject.duration);
        progressBar.style.width = (musicObject.currentTime * 100)/musicObject.duration +"%"
    }
    musicObject.addEventListener("play", () => {
        play.innerHTML = '<span class="fas fa-pause"></span ';
        cover.classList.add("rotate360");
        console.log("event play");
    })
    musicObject.addEventListener("pause", () => {
        play.innerHTML = '<span class="fas fa-play"></span ';
        cover.classList.remove("rotate360");
        console.log("event play");
    })
};

let setActualSong = (index) => {
    title.innerHTML = songs[index].title;
    cover.setAttribute("src", songs[index].img);
    music = new Audio(songs[index].url + songs[index].title + songs[index].ext);
    setEventListeners(music);
};

let isPaused = () => {
    if(music.paused){
        return true;
    }else{
        music.pause()
        return false;
    }
}

last.addEventListener("click", (e) => {
    console.log("Button Last");
    actual--;
    isPaused();
    if(actual == -1){
        actual = songs.length - 1;
    }
    setActualSong(actual);
    music.play();
});

play.addEventListener("click", (e) => {
    console.log("Button Play");
    if(isPaused()){
        music.play();
    }
});

next.addEventListener("click", (e) => {
    console.log("Button Next");
    actual++;
    isPaused();
    if(actual == songs.length){
        actual = 0;
    }
    setActualSong(actual);
    music.play();
});

setActualSong(actual);
