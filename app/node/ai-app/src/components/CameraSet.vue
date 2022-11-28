<template>
  <div>
    <video ref="video" id="video" width="500" height="500" autoplay></video>
    <div>
      <button color="info" id="snap" v-on:click="capture()">Snap Photo</button>
    </div>
    <canvas ref="canvas" id="canvas" width="500" height="500"></canvas>
    <ul>
    <li class="capture" v-for="c in captures" v-bind:key="c.d">
      <img v-bind:src="c" height="50" />
    </li>
    </ul>
  </div>
</template>


<script>

export default {
  name: 'CameraSet',
  mounted () {
    this.video = this.$refs.video
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      navigator.mediaDevices.getUserMedia({ video: true }).then(stream => {
        this.video.srcObject = stream
        this.video.play()
      })
    }
  },
  methods: {
    capture () {
          this.canvas = this.$refs.canvas
          this.canvas.getContext('2d').drawImage(this.video, 0, 0, 500, 500)
          //const captures = 
          //this.captures.push(this.canvas.toDataURL('image/png'))
          console.log(this.canvas.toDataURL('image/png'))
        }
  },

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
