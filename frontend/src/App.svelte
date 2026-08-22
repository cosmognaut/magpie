<script lang="ts">
	import Home from './lib/Home.svelte'
	import Why from './lib/Why.svelte'
	import How from './lib/How.svelte'
	let page: string = $state('home'); // keeps track of the current page

	function checkHome() {
		const currentURL = String(window.location.pathname);
		const currentPage = currentURL.slice(currentURL.indexOf('/') + 1, );
		if (currentPage !== '') page = currentPage;
		else page = 'home'; // if it says nothing after the last '/', we are at the home page.
	}

	function updatePage(event: MouseEvent & { currentTarget: EventTarget & HTMLButtonElement}, name: string) {
		event.preventDefault();
		history.pushState(null, "", name);
		page = name;
	}

	// also check the URL on startup (after reloads) so that we know if we are on the home page or not
	checkHome();
</script>

<svelte:window onpopstate={checkHome} />
<!-- FIXME: the dots when applied here look a bit off. Might I want a header component? -->
<div class="">
	<nav class="md:flex flex-row justify-center items-center p-0.5 gap-100 mt-5 text-center">	
		<button class="font-mono font-bold hover:text-emerald-500 cursor-pointer transition-colors" onclick={(event) => updatePage(event, 'why')}>[ WHY? ]</button>
		<button class="font-mono font-bold hover:text-emerald-500 cursor-pointer transition-colors" onclick={(event) => updatePage(event, 'home')}>[ HOME ]</button>
		<button class="font-mono font-bold hover:text-emerald-500 cursor-pointer transition-colors" onclick={(event) => updatePage(event, 'how')}>[ HOW? ]</button>
	</nav>
</div>
{#if page === 'home'}
	<Home />
{:else if page === 'why'}
	<Why />
{:else if page === 'how'}
	<How />
{/if}

<footer class="mt-10 ml-4 mb-4 text-center">
 <p>A cosmognaut production.</p>
</footer>

<!-- copied from Home.svelte, see that for more details -->
<style>
	.dots {
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
