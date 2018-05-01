let factors =[];

function isPrimeFactor(n) {
	for (var i = 2; i <= n; i++) {
		if (n%i===0) {
			n=n/i;
			factors.push(i);

		} else {
			i = i +1;

		}
		
	}
}
isPrimeFactor(600851475143);
console.log(Math.max(factors));