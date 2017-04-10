function addPersonMethods (person) {
	if (this instanceof addPersonMethods){
			this.name = person.name;  
			this.age = person.age;
	}
	else {
		return new addPersonMethods(person);
	}
	
    this.greet = function (greeting) {
        console.log(greeting + ", my name is " + this.name );
    };
	
	this.compareAge = function(newPerson) {
		if (this.age == newPerson.age)
			console.log("My name is " + this.name + " and I'm equally young as " + newPerson.name );
		if (this.age > newPerson.age)
			console.log("My name is " + this.name + " and I'm older than " + newPerson.name );
		if (this.age < newPerson.age)
			console.log("My name is " + this.name + " and I'm younger than " + newPerson.name );
	};
	
    this.namesake = function (newPerson) {
		if (this.name == newPerson.name)
			console.log("We have the same name, " + this.name + " and I!" );
		else
			console.log("We have different names, " + newPerson.name + " and I." );
    };
	
}


