<script lang="ts">
	let { title, thumbnail, duration, channelName, views } = $props();
	import { formatISO, formatViews } from '../utils.svelte'
</script>

<div class="border w-110 h-75 flex-none py-2 px-2 relative hover:border-emerald-500 transition-colors">
	<!-- <a href="https://www.youtube.com/watch?v=yxSd-lcmbGY"> -->
		<img src={thumbnail} alt="video thumbnail" class="w-full h-4/5 grayscale hover:grayscale-0 transition" loading="lazy">
		<p class="bg-black absolute bottom-15 right-2 p-1">{formatISO(duration)}</p>
		<p class="mt-1 font-mono font-semibold line-clamp-1">{title}</p>
		<div class="video-info flex flex-row justify-between">
			<p class="mb-1 font-mono font-light">{channelName}</p>
			<p class="font-mono font-light">{formatViews(views)} views</p>
		</div>
	<!-- </a> -->
</div>
