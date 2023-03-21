<template>
  <div>
    <h1>Top page</h1>
    <div><button class="button" @click="logout()">Logout</button></div>
    <!--<video ref="video" id="video" width="500" height="500" autoplay></video>-->
    <!--<div>
      <button color="info" id="snap" v-on:click="capture()">Snap Photo</button>
    </div>-->
    <input ref="upfile" type="file" v-on:change="imageToBase64"/><br/><br/>
    <img  class="inline object-center " v-if="showPrev" v-bind:src="previewBase64" alt="preview" width="300"/><br/><br/>
    <!--<canvas ref="canvas" id="canvas" width="500" height="500"></canvas>
    ul>
    <li class="capture" v-for="c in captures" v-bind:key="c.d">
      <img v-bind:src="c" height="50" />
    </li>
    </ul>-->
  </div>
</template>


<script>

export default {
  name: 'CameraSet',
  data(){
    return{
      showPrev: false,
      previewBase64: ''
    }
   
  },

 
  /*mounted () {
    this.video = this.$refs.video
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      navigator.mediaDevices.getUserMedia({ video: true }).then(stream => {
        this.video.srcObject = stream
        this.video.play()
      })
    }
  },*/
  methods: {
    logout () {
      return this.$store.dispatch('logout')
        .then(() => {
          this.$router.push('/login')
        })
        .catch(error => { throw error })
    },
    capture () {
          this.canvas = this.$refs.canvas
          this.canvas.getContext('2d').drawImage(this.video, 0, 0, 500, 500)
          //const captures = 
          //this.captures.push(this.canvas.toDataURL('image/png'))
          console.log(this.canvas.toDataURL('image/png'))
    },
    imageToBase64(event){
      const reader = new FileReader()

      // 選択されたファイルの取得
      const file = event.target.files[0]

      // ファイルが選択されていればBase64に変換する
      if(file){
        reader.readAsDataURL(file)
      }else{
        this.previewBase64 = ''
      }

      // 変換が終わったら実行される
      reader.onload = () => {
        this.showPrev = true
        this.previewBase64 = reader.result
      }
    },

  },

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
