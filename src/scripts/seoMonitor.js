/**
 * SEO Monitoring System for fullstacksmsts.co.uk
 * This script monitors SEO metrics and competitor changes.
 */

class SEOMonitor {
  constructor(config) {
    this.config = config || {
      website: 'https://fullstacksmsts.co.uk',
      notificationEmail: 'seo@fullstacksmsts.co.uk',
      rankDropThreshold: 5, // Alert if ranking drops by this many positions
      trafficDropThreshold: 15, // Alert if traffic drops by this percentage
      competitors: [
        { name: 'SMSTS Course', url: 'https://www.smstscourse.co.uk' },
        { name: 'Knight Learning', url: 'https://www.knightlearning.co.uk' },
        { name: 'Tam Training', url: 'https://www.tamtraining.co.uk' },
        { name: 'Goldcross Training', url: 'https://www.goldcrosstraining.co.uk' },
        { name: 'SafetyMark Training', url: 'https://www.safetymarktraining.co.uk' },
        { name: '3B Training', url: 'https://www.3btraining.com' },
        { name: 'NATAS', url: 'https://www.natas.co.uk' },
        { name: 'SAMS Ltd', url: 'https://www.samsltd.co.uk' }
      ],
      keywordsToMonitor: [
        'SMSTS course online',
        'SMSTS course London',
        'SMSTS weekend course',
        'SMSTS refresher course',
        'CITB SMSTS course',
        'SMSTS course price',
        'SMSTS translation services',
        'Site management safety training'
      ]
    };
    
    this.dataStore = {
      rankings: [],
      traffic: [],
      competitorChanges: []
    };
    
    console.log('SEO Monitor initialized');
  }
  
  /**
   * Monitor keyword rankings
   */
  async monitorKeywordRankings() {
    console.log('Monitoring keyword rankings...');
    
    try {
      // In a real implementation, this would call a rank tracking API
      // For example, using SEMrush, Ahrefs, or a custom scraping solution
      
      // Mock implementation
      const rankings = this.config.keywordsToMonitor.map(keyword => {
        return {
          keyword,
          currentRank: Math.floor(Math.random() * 20) + 1,
          previousRank: Math.floor(Math.random() * 20) + 1,
          url: `${this.config.website}/${keyword.toLowerCase().replace(/\s+/g, '-')}`,
          date: new Date().toISOString()
        };
      });
      
      // Store rankings data
      this.dataStore.rankings = rankings;
      
      // Check for significant ranking changes
      const significantChanges = rankings.filter(
        r => r.previousRank - r.currentRank >= this.config.rankDropThreshold
      );
      
      if (significantChanges.length > 0) {
        this._sendAlert('Ranking Drops Detected', 
          `The following keywords have dropped in rankings:\n
          ${significantChanges.map(r => 
            `${r.keyword}: from position ${r.previousRank} to ${r.currentRank}`
          ).join('\n')}`
        );
      }
      
      console.log(`Monitored ${rankings.length} keywords`);
      return rankings;
      
    } catch (error) {
      console.error('Error monitoring keyword rankings:', error);
      return [];
    }
  }
  
  /**
   * Monitor website traffic
   */
  async monitorTraffic() {
    console.log('Monitoring website traffic...');
    
    try {
      // In a real implementation, this would call Google Analytics API
      // or another analytics platform
      
      // Mock implementation
      const today = new Date();
      const traffic = {
        date: today.toISOString(),
        source: 'organic',
        sessions: Math.floor(Math.random() * 500) + 100,
        users: Math.floor(Math.random() * 450) + 90,
        pageViews: Math.floor(Math.random() * 1200) + 300,
        bounceRate: (Math.random() * 0.3 + 0.4).toFixed(2),
        avgSessionDuration: Math.floor(Math.random() * 180) + 60
      };
      
      // Store traffic data
      this.dataStore.traffic.push(traffic);
      
      // Compare with previous period if available
      if (this.dataStore.traffic.length > 1) {
        const previousTraffic = this.dataStore.traffic[this.dataStore.traffic.length - 2];
        const trafficChange = ((traffic.sessions - previousTraffic.sessions) / previousTraffic.sessions) * 100;
        
        if (trafficChange <= -this.config.trafficDropThreshold) {
          this._sendAlert('Traffic Drop Detected', 
            `Organic traffic has dropped by ${Math.abs(trafficChange).toFixed(1)}% compared to the previous period.
            Current sessions: ${traffic.sessions}
            Previous sessions: ${previousTraffic.sessions}`
          );
        }
      }
      
      console.log('Traffic monitoring completed');
      return traffic;
      
    } catch (error) {
      console.error('Error monitoring traffic:', error);
      return null;
    }
  }
  
  /**
   * Monitor competitor changes
   */
  async monitorCompetitors() {
    console.log('Monitoring competitor changes...');
    
    try {
      // In a real implementation, this would scrape competitor websites
      // or use a service like Visualping or Distill.io
      
      // Mock implementation
      const competitorChanges = [];
      
      for (const competitor of this.config.competitors) {
        // Simulate finding changes on some competitors
        if (Math.random() > 0.7) {
          competitorChanges.push({
            competitor: competitor.name,
            url: competitor.url,
            changeType: Math.random() > 0.5 ? 'content' : 'pricing',
            description: Math.random() > 0.5 
              ? 'New course offering detected' 
              : 'Price change detected',
            date: new Date().toISOString()
          });
        }
      }
      
      // Store competitor changes
      this.dataStore.competitorChanges = competitorChanges;
      
      if (competitorChanges.length > 0) {
        this._sendAlert('Competitor Changes Detected',
          `Changes detected on ${competitorChanges.length} competitor websites:\n
          ${competitorChanges.map(c => 
            `${c.competitor}: ${c.description} (${c.changeType})`
          ).join('\n')}`
        );
      }
      
      console.log(`Monitored ${this.config.competitors.length} competitors, found ${competitorChanges.length} changes`);
      return competitorChanges;
      
    } catch (error) {
      console.error('Error monitoring competitors:', error);
      return [];
    }
  }
  
  /**
   * Run all monitoring tasks
   */
  async runFullMonitoring() {
    console.log('Starting full SEO monitoring process...');
    
    await this.monitorKeywordRankings();
    await this.monitorTraffic();
    await this.monitorCompetitors();
    
    console.log('Full SEO monitoring completed');
    return {
      rankings: this.dataStore.rankings,
      traffic: this.dataStore.traffic,
      competitorChanges: this.dataStore.competitorChanges
    };
  }
  
  /**
   * Send alert notification
   * @private
   */
  _sendAlert(subject, message) {
    // In a real implementation, this would send an email or other notification
    console.log(`ALERT: ${subject}`);
    console.log(message);
    
    // Mock email sending
    console.log(`Alert email would be sent to ${this.config.notificationEmail}`);
  }
}

// Export the SEOMonitor class
export default SEOMonitor;

// Example usage:
// const monitor = new SEOMonitor();
// monitor.runFullMonitoring();
