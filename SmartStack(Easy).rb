class Stack
	def initialize()
		@next = nil
		@value = nil
	end
	
	def next
		@next
	end
	
	def value
		@value
	end
	
	def setValue(val)
		@value = val
	end
	
	def setNext(val)
		@next = val
	end

	def push(item)
		if self.value==nil
			self.setValue(item)
		else
			newt = Stack.new()
			newt.setValue(self.value)
			newt.setNext(self.next)
			self.setValue(item)
			self.setNext(newt)
		end
	end
	
	def pop()
		retVal = self.value
		self.setValue(nil)
		if(self.next!=nil)
			self.setValue(self.next.value)
			self.setNext(self.next.next)
		end
		return retVal
	end

	def display()
		puts self.to_s
	end
	
	def to_s
		retStr = "["
		cur = self
		while(cur!=nil && cur.value!=nil)
			retStr+=cur.value.to_s+", "
			cur = cur.next
		end
		if(retStr.length>1)
			retStr = retStr[0..-3]
		end
		return retStr+"]"
	end
end

class SortStack < Stack
	def push(item)
		if self.value==nil
			self.setValue(item)
		elsif self.value < item
			temp = self.value
			self.setValue(item)
			newt = SortStack.new()
			newt.setNext(@next)
			newt.setValue(temp)
			self.setNext(newt)
		else
			if(self.next==nil)
				self.setNext(SortStack.new())
			end
			self.next.push(item)
		end
	end
	
	def remove(value)
		if(self.value==value)
			self.setValue(nil)
			if(self.next!=nil)
				self.setValue(self.next.value)
				self.setNext(self.next.next)
				return true
		elsif self.next!=nil
			return self.next.remove(value)
		end
		return false
	end
end
end

class SmartStack
	def initialize
		@sorted = SortStack.new()
		@default = Stack.new()
		@size = 0
	end
	
	def push(val)
		@sorted.push(val)
		@default.push(val)
		@size+=1
	end
	
	def pop()
		if(@size>0)
			temp = @default.pop()
			@sorted.remove(temp)
			@size-=1
			return temp
		end
	end
	
	def size
		return @size
	end
	
	def displayStack()
		@default.display()
	end
	
	def displayOrdered()
		@sorted.display()
	end
end

def main()
	stack = SmartStack.new()
	stack.push(1)
	stack.push(28)
	stack.push(13)
	stack.push(4)
	stack.push(3)
	stack.displayOrdered()
	stack.displayStack()
end

main()