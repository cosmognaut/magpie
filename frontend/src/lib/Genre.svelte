<script lang="ts">
	import Video from './Video.svelte'
	import { fade } from 'svelte/transition'

	let { name } = $props();
	let scrolled: boolean = $state(false);
	let element: Element;
	const scrollValue: number = 600;
	// element is a reference to a DOM node which contains the element on which we want to scroll
	function scrollRight(){
		element.scrollBy({
		  top: 0,
		  left: scrollValue,
		  behavior: "smooth",
		});
		scrolled = true;
	}

	function scrollLeft(){
		console.log(element.scrollLeft);
		element.scrollBy({
		  top: 0,
		  left: -scrollValue,
		  behavior: "smooth",
		});
		if (element.scrollLeft <= scrollValue) {
			scrolled = false;
		}
	}
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
<div class="grid auto-rows-max gap-3 mt-10 relative">
	<h2 class="font-medium text-4xl px-4 font-display">{name}</h2>
	<p class="px-4 font-mono">This is some text related to the genre..</p>
	{#if scrolled}
		<button class="absolute top-[55%] left-1 bg-emerald-700 rounded-none p-3 hover:bg-emerald-800 cursor-pointer border rotate-180 z-10" aria-label="Scroll" onclick={scrollLeft} transition:fade>
			<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#fef3c6" d="M16.15 13H5q-.425 0-.712-.288T4 12t.288-.712T5 11h11.15L13.3 8.15q-.3-.3-.288-.7t.288-.7q.3-.3.713-.312t.712.287L19.3 11.3q.15.15.213.325t.062.375t-.062.375t-.213.325l-4.575 4.575q-.3.3-.712.288t-.713-.313q-.275-.3-.288-.7t.288-.7z"/></svg>
		</button>
	{/if}
 	<div class="grid grid-flow-col gap-5 p-3 w-auto overflow-auto mr-4 ml-4 px-4 border" bind:this={element}>
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
	<button class="absolute top-[55%] right-1 bg-emerald-700 rounded-none p-3 hover:bg-emerald-800 cursor-pointer border" aria-label="Scroll" onclick={scrollRight}>
		<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="#fef3c6" d="M16.15 13H5q-.425 0-.712-.288T4 12t.288-.712T5 11h11.15L13.3 8.15q-.3-.3-.288-.7t.288-.7q.3-.3.713-.312t.712.287L19.3 11.3q.15.15.213.325t.062.375t-.062.375t-.213.325l-4.575 4.575q-.3.3-.712.288t-.713-.313q-.275-.3-.288-.7t.288-.7z"/></svg>
	</button>
</div>
