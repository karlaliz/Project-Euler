function fibonacci(){
	let first = 0;
	let second = 1;
	let next = 1;
	let add=0;
	while(next <=4*1000*1000) {
		next = first +second;
		if (next % 2 ===0){
			add+= next;
		};

		first = second;
		second = next;	
	};
	return add;
};
console.log(fibonacci());