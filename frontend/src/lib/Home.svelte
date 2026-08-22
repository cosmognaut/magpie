<script lang="ts">
	import Header from './Header.svelte'
	import Search from './Search.svelte'
	import Genre from './Genre.svelte'
	import { count, shuffle } from '../utils.svelte'
	import type { Video } from '../utils.svelte'

	let query: string = $state(''); // user query inside the search box
	let statistics: [Array<string>, number] = $state([[''], 0]);
	let found: Array<string> = $derived(statistics[0].filter((genre: string) => (genre.toLowerCase()).includes(query))); // found genres

	let focusElement: Search; // the component instance we need access to
	let keyCombinationCanHappen: boolean = false; // for CTRL-K, see advancedSearch
	let keyCombinationActivated: boolean = false;

	const API_URL = 'https://magpie.ishu.foo/videos/'; // using the main URL
	let data;

	// credit: https://gist.github.com/meain/6440b706a97d2dd71574769517e7ed32
	const LOADING_MESSAGES = [
		"In space no one can hear you cry TT",
		"Are we there yet?",
		"Pokémon Emerald is the best pokémon game <3",
		"The minions are doing their work..",
		"I promise it's almost done..",
		"Dividing by zero...",
		"The British are coming!",
		"I prefer the muddy water...",
		"No animals harmed during the making of this..",
		"Slay the mighty set!",
		"WHOLE NEW WORLD",
	]

	function onInput(event: Event & { currentTarget: EventTarget & HTMLInputElement }) {
		// convert the user's query in the search bar to lower case and assign it to state
		query = event.currentTarget.value.toLowerCase();
	}

	function advancedSearch(event: KeyboardEvent) {
		// this is for CTRL-K. Prevent the default behaviour which would be focusing on the browser-default search bar.
		// we call focus() on the focusElement, which is a reference to the Search component instance.

		// for debugging
		// console.log(event.key);
		if (event.key === 'Control') keyCombinationCanHappen = true;
		if (keyCombinationCanHappen && event.key === 'k') {
			// console.log(keyCombinationCanHappen);
			keyCombinationActivated = true;
			event.preventDefault();
			focusElement.callFocus();
		}
		if (keyCombinationActivated) {
			// reset everything back to original values if key combination was activated to await future combinations
			keyCombinationCanHappen = false;
			keyCombinationActivated = false;
		}
	}

	// we need to interact with the world outside of Svelte's reactivity - the DOM
	// hence, we use an effect here
	$effect( () => {
		document.addEventListener('keydown', advancedSearch);

		return () => {
			removeEventListener('keydown', advancedSearch);
		}
	});

	async function fetchFromEndpoint(): Promise<any> {
		/*
		* Fetch data from the API and return a promsie that will be resolved by the await block
		*/
		let response = await fetch(API_URL); // waits for the promise to resolve because of await
		const data = await response.json(); // waits for the promise to resolve again
		return data; // the final JSON object promise - this needs to be awaited too to get the final object!
		// return await response.json(); is also totally valid!
	}

	const fetchPromise: Promise<any> = fetchFromEndpoint(); // this needs to be awaited
	let videoList: Array<Video[]> = $state([]); // I made this a state because Svelte was giving me this error: non_reactive_update
	// do this AFTER the promise resolves
	fetchPromise.then( (result) => {
		data = result;
		let returned = count(data);
		statistics[0] = returned[0];
		statistics[1] = returned[1];
		videoList = returned[2];
	})
	// see https://zhangpascal.medium.com/how-to-properly-type-event-handlers-in-svelte-with-typescript-8e098c756eb9 on how to type event handlers.
</script>

<div class="dots">
	<Header statistics={statistics}/>
</div>

<Search onInput={onInput} bind:this={focusElement}/>

{#await fetchPromise}
	<p class="text-2xl text-center mt-10">{LOADING_MESSAGES[Math.floor(Math.random() * LOADING_MESSAGES.length)]}</p>
{:then data}
	<!-- when there's no input, found is still the entire genreList -->
	{#if found.length !== 0}
		{#each shuffle(found) as genre}
			<Genre name={genre} videos={videoList[statistics[0].indexOf(genre)]}/>
		{/each}
	{:else}
		<div class="mt-12 mb-4 ml-4 w-100vw h-100vh">
			 <p class="text-4xl text-center font-light">We don't have that genre!</p>
			 <p class="text-xl text-center mt-2 font-extralight">Watch something else, maybe?</p>
		</div>
	{/if}
{:catch error}
	<p class="text-2xl text-center mt-10">Failed to fetch data. FastAPI is not so fast maybe? Error: {error}</p>
{/await}

<style>
	.dots {
		/*
		# Drawing a grid 101
			Let's see what's happening here: a linear gradient works in such a way that it gets a direction, and two colors from you. Then by default it goes from top to bottom, but you could also have it go along the x-axis via a 90 degree rotation - that's the first argument. Here, let's look at everything line by line:
			background-size: 80px 80px - we reserve a canvas of 80px from left to right (width) and 80px from top to bottom (height) as we want to draw two gradients here. We do this for all 3 layers.
			background-position: center - we center the reserved canvas
			background: three layers to this:-
				- we draw a black linear gradient till 79px in an 80px canvas, and then draw a transparent color at the same 79th pixel. Now because these two values are the same, and the canvas is only of 80px in size, we hit a stop and for the remaining pixels (80-79 = 1px) we draw a transparent line. This means that this creates a horizontal transparent line across the bottom edge of the box. But why do we draw a line for the remaining one pixel, why not anything else? Here's it's useful to keep in mind the "fill-to-end" rule in CSS - A CSS gradient will always stretch to completely fill its canvas. Even though we stopped giving the browser instructions at 79px, the canvas keeps going until 80px. Because we didn't tell the brwoser what to do after 79px, the browser follows the default rule and takes the very last color we gave and stretches it all the way to the end. Here that very last color is 'transparent'.
				- we first rotate the gradient by 90 degrees to align it with the x-axis. We do the same thing as we did in the first gradient, it's just that this time it's rotated by 90 degrees. This means that this creates a vertical line at the right edge of the box.
				- the last argument to background is a solid white color (with an opacity of 0.55). The solid background represents the base canvas of the layers and fills the entire screen. It means that whatever the intersection of the first two gradients was, takes this color. This means that our tiny 1px dots will be this slightly off-white in color.
		*/
		background: linear-gradient(black 79px, transparent 79px), linear-gradient(90deg, black 79px, transparent 79px), rgba(255, 255, 255, 0.65);
	  	background-position: center;
	  	background-size: 80px 80px, 80px 80px, 80px 80px;
		animation: infinite-loop 2000ms linear infinite;
  }
  
  @keyframes infinite-loop {
	from {
		background-position: 0px 0px; /* move from (0, 0)*/
		}
	to {
		background-position: 0px 80px; /* to (0, 80) - this creates a vertical shower-like animation*/
	}
  }
</style>
