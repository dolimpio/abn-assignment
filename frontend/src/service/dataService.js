import axios from 'axios'

const URI = 'http://localhost:8000/data'

function transformData(data) {
  const map = new Map()

  // Create a map of nodes indexed by their name
  data.forEach((item) => {
    map.set(item.name, { label: item.name, data: { description: item.description }, children: [] })
  })

  // Build the hierarchy based on the parent-child relationship and generate keys
  data.forEach((item) => {
    const node = map.get(item.name)
    const parent = item.parent ? map.get(item.parent) : null

    if (parent) {
      parent.children.push(node)
    }

    // Generate key based on parent-child relationship
    if (parent) {
      const keyPrefix = parent.key ? parent.key + '_' : ''
      const childIndex = parent.children.length
      node.key = keyPrefix + childIndex
    } else {
      node.key = '0' // Set root node key
    }
  })

  // Return the root node only
  return map.get('A')
}

// Fetches data
export const fetchData = async () => {
  try {
    const response = await axios.get(URI)
    console.log('inside fetch data')
    console.log(response.data)
    // The the data array is under 'data' key
    const responseData = response.data.data
    // Convert hierarchy object into array
    const transformedData = transformData(responseData)
    console.log('trasnformed data')
    console.log(transformedData)
    return transformedData
  } catch (error) {
    console.error('Error fetching data:', error)
    throw error
  }
}
