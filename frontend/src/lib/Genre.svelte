<script lang="ts">
	import Video from './Video.svelte'
</script>
<!---->
<!-- <div class="flex flex-col items-start gap-2 p-4 my-7"> -->
<!-- 	<h2 class="font-medium text-xl">Philosophy</h2> -->
<!-- 	<div class="flex flex-row gap-10 border p-3 w-345 flex-nowrap overflow-auto"> -->
<!-- 		<Video></Video> -->
<!-- 		<Video></Video> -->
<!-- 		<Video></Video> -->
<!-- 		<Video></Video> -->
<!-- 		<Video></Video> -->
<!-- 		<Video></Video> -->
<!-- 		<Video></Video> -->
<!-- 	</div> -->
<!-- </div> -->
<!---->
<div class="grid auto-rows-max gap-3 mt-5">
	<h2 class="font-medium text-4xl px-4 font-display">Genre</h2>
		<p class="px-4 font-mono">This is some text related to the genre..</p>
 		<div class="grid grid-flow-col gap-5 p-3 w-auto overflow-auto mr-4 ml-4 px-4 border">
			<Video></Video>
			<Video></Video>
			<Video></Video>
			<Video></Video>
			<Video></Video>
			<Video></Video>
			<Video></Video>
			<Video></Video>
			<Video></Video>
			<Video></Video>
			<Video></Video>
 		</div>
</div>
