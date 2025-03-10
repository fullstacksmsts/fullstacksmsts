import React from 'react';
import { Link } from 'react-router-dom';
import { blogPosts } from '../../data/blogPosts';

const HomePage = () => {
  // Get the latest 3 blog posts
  const latestPosts = blogPosts.slice(0, 3);

  return (
    <div>
      {/* Hero Section */}
      <section className="bg-[var(--primary-blue)] text-white py-16 rounded-lg mb-16">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8">
          <div className="md:flex items-center">
            <div className="md:w-1/2 mb-8 md:mb-0">
              <h1 className="text-4xl md:text-5xl font-bold mb-4">
                CITB SMSTS Courses with 98% Pass Rate
              </h1>
              <p className="text-xl mb-8">
                Flexible online, weekend, and weekday SMSTS courses at just £360+VAT. 
                Translation services available in any language.
              </p>
              <div className="flex flex-col sm:flex-row gap-4">
                <Link 
                  to="/book-course" 
                  className="bg-[var(--cta-orange)] hover:bg-[var(--orange-accent)] text-white font-medium py-3 px-6 rounded-lg text-center transition duration-150"
                >
                  Book SMSTS Course
                </Link>
                <Link 
                  to="/contact" 
                  className="bg-transparent hover:bg-white hover:text-[var(--primary-blue)] text-white border border-white font-medium py-3 px-6 rounded-lg text-center transition duration-150"
                >
                  Request a Callback
                </Link>
              </div>
            </div>
            <div className="md:w-1/2">
              <img 
                src="/api/placeholder/600/400" 
                alt="SMSTS Training" 
                className="rounded-lg shadow-lg"
              />
            </div>
          </div>
        </div>
      </section>

      {/* Course Types Section */}
      <section className="mb-16">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold text-center text-[var(--primary-blue)] mb-12">
            Flexible SMSTS Course Options
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {/* Weekend Course */}
            <div className="bg-white rounded-xl shadow-lg p-6 hover:shadow-xl transition-shadow">
              <div className="bg-[var(--primary-blue)] text-white p-4 rounded-lg inline-block mb-4">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                </svg>
              </div>
              <h3 className="text-xl font-bold mb-2">Weekend Courses</h3>
              <p className="text-gray-600 mb-4">
                Complete your SMSTS training over two weekends plus one Friday, 
                minimizing disruption to your work schedule.
              </p>
              <Link 
                to="/courses/weekend" 
                className="text-[var(--cta-orange)] hover:text-[var(--orange-accent)] font-medium flex items-center"
              >
                Learn more
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 ml-1" viewBox="0 0 20 20" fill="currentColor">
                  <path fillRule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clipRule="evenodd" />
                </svg>
              </Link>
            </div>
            
            {/* Weekday Course */}
            <div className="bg-white rounded-xl shadow-lg p-6 hover:shadow-xl transition-shadow">
              <div className="bg-[var(--primary-blue)] text-white p-4 rounded-lg inline-block mb-4">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
                </svg>
              </div>
              <h3 className="text-xl font-bold mb-2">Weekday Courses</h3>
              <p className="text-gray-600 mb-4">
                Traditional 5-day block course, completed Monday to Friday, 
                or day release options available.
              </p>
              <Link 
                to="/courses/weekday" 
                className="text-[var(--cta-orange)] hover:text-[var(--orange-accent)] font-medium flex items-center"
              >
                Learn more
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 ml-1" viewBox="0 0 20 20" fill="currentColor">
                  <path fillRule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clipRule="evenodd" />
                </svg>
              </Link>
            </div>
            
            {/* Online Course */}
            <div className="bg-white rounded-xl shadow-lg p-6 hover:shadow-xl transition-shadow">
              <div className="bg-[var(--primary-blue)] text-white p-4 rounded-lg inline-block mb-4">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                </svg>
              </div>
              <h3 className="text-xl font-bold mb-2">Online Courses</h3>
              <p className="text-gray-600 mb-4">
                Complete your SMSTS training remotely with live instructor support, 
                saving travel time and expenses.
              </p>
              <Link 
                to="/courses/online" 
                className="text-[var(--cta-orange)] hover:text-[var(--orange-accent)] font-medium flex items-center"
              >
                Learn more
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 ml-1" viewBox="0 0 20 20" fill="currentColor">
                  <path fillRule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clipRule="evenodd" />
                </svg>
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* Why Choose Us Section */}
      <section className="mb-16 bg-gray-50 py-16 rounded-lg">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold text-center text-[var(--primary-blue)] mb-12">
            Why Choose FullStack SMSTS?
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            {/* Feature 1 */}
            <div className="text-center">
              <div className="bg-[var(--primary-blue)] text-white p-4 rounded-full inline-flex items-center justify-center w-16 h-16 mb-4">
                <span className="text-2xl font-bold">98%</span>
              </div>
              <h3 className="text-xl font-bold mb-2">High Pass Rate</h3>
              <p className="text-gray-600">
                Our expert trainers ensure you have the best chance of success with our 98% pass rate.
              </p>
            </div>
            
            {/* Feature 2 */}
            <div className="text-center">
              <div className="bg-[var(--primary-blue)] text-white p-4 rounded-full inline-flex items-center justify-center w-16 h-16 mb-4">
                <span className="text-2xl font-bold">£</span>
              </div>
              <h3 className="text-xl font-bold mb-2">Competitive Pricing</h3>
              <p className="text-gray-600">
                At just £360+VAT, our courses offer excellent value without compromising on quality.
              </p>
            </div>
            
            {/* Feature 3 */}
            <div className="text-center">
              <div className="bg-[var(--primary-blue)] text-white p-4 rounded-full inline-flex items-center justify-center w-16 h-16 mb-4">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 5h12M9 3v2m1.048 9.5A18.022 18.022 0 016.412 9m6.088 9h7M11 21l5-10 5 10M12.751 5C11.783 10.77 8.07 15.61 3 18.129" />
                </svg>
              </div>
              <h3 className="text-xl font-bold mb-2">Translation Services</h3>
              <p className="text-gray-600">
                We offer translation services in any language to ensure everyone can access our training.
              </p>
            </div>
            
            {/* Feature 4 */}
            <div className="text-center">
              <div className="bg-[var(--primary-blue)] text-white p-4 rounded-full inline-flex items-center justify-center w-16 h-16 mb-4">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                </svg>
              </div>
              <h3 className="text-xl font-bold mb-2">CITB Accredited</h3>
              <p className="text-gray-600">
                All our courses are fully CITB accredited, ensuring your certification is recognized industry-wide.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Latest Blog Posts Section */}
      <section className="mb-16">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center mb-8">
            <h2 className="text-3xl font-bold text-[var(--primary-blue)]">
              Latest Blog Posts
            </h2>
            <Link 
              to="/blog" 
              className="text-[var(--cta-orange)] hover:text-[var(--orange-accent)] font-medium flex items-center"
            >
              View all posts
              <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 ml-1" viewBox="0 0 20 20" fill="currentColor">
                <path fillRule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clipRule="evenodd" />
              </svg>
            </Link>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {latestPosts.map(post => (
              <div key={post.id} className="bg-white rounded-xl shadow-lg overflow-hidden transition-transform hover:scale-105">
                <Link to={`/blog/${post.id}`}>
                  <img 
                    src={post.featuredImage} 
                    alt={post.title} 
                    className="w-full h-48 object-cover"
                  />
                </Link>
                <div className="p-6">
                  <div className="flex items-center text-sm text-gray-500 mb-2">
                    <span className="bg-blue-100 text-blue-800 px-2 py-1 rounded">{post.category}</span>
                    <span className="mx-2">•</span>
                    <span>{post.readTime}</span>
                  </div>
                  <Link to={`/blog/${post.id}`} className="block mt-2">
                    <h3 className="text-xl font-bold text-gray-900 hover:text-[var(--cta-orange)]">{post.title}</h3>
                  </Link>
                  <p className="mt-3 text-gray-600 line-clamp-2">
                    {post.subtitle}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="bg-[var(--primary-blue)] text-white rounded-xl p-8 shadow-lg mb-16">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8">
          <div className="md:flex items-center justify-between">
            <div className="md:w-2/3">
              <h2 className="text-2xl font-bold mb-4">Ready to advance your construction career?</h2>
              <p className="mb-6 md:mb-0">
                Book your SMSTS course today with fullstacksmsts.co.uk. With a 98% pass rate and competitive pricing of just £360+VAT, we're the trusted choice for SMSTS training across the UK.
              </p>
            </div>
            <div className="md:w-1/3 text-center md:text-right">
              <Link 
                to="/book-course" 
                className="inline-block bg-[var(--cta-orange)] hover:bg-[var(--orange-accent)] text-white font-medium py-3 px-6 rounded-lg transition duration-150"
              >
                Book SMSTS Course
              </Link>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default HomePage;
